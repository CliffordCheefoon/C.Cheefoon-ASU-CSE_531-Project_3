import grpc
from branch import branch_client_stub
from services.gprc_coms import branch_pb2_grpc
from services.gprc_coms import branch_pb2
from services.gprc_coms.branch_pb2 import branchEventRequest, branchEventResponse               # pylint: disable=no-name-in-module
from services.input_parser.parser import branch_input, event


class event_mutate_response:                                                                           # pylint: disable=invalid-name
    """Data Representation Class: Customer events that mutate the balance"""
    def __init__(self, interface: str, result ):
        self.interface = interface
        self.result = result

class event_query_response:                                                                           # pylint: disable=invalid-name
    """Data Representation Class: Customer Query"""
    def __init__(self, interface: str, result ):
        self.interface = interface
        self.balance = result

class customer_response:                                                                        # pylint: disable=invalid-name
    """Data Representation Class: Customer with events"""
    def __init__(self, incoming_id : int , recv : list):
        self.id = incoming_id
        self.recv = recv

class Customer:
    """A customer with it's own GRPC stub to it's own Branch Server"""
    events: list[event]
    def __init__(self, id: int, branch_metadata_list : list[branch_input]):     # pylint: disable=redefined-builtin
        # unique ID of the Customer
        self.id = id
        # a list of received messages used for debugging purpose
        self.recvMsg: list = []                                                 # pylint: disable=invalid-name
        # pointer for the stub
        self.stub_list = self.createStubs(branch_metadata_list)
        self.last_write_id  = 0

    def soft_reset(self):
        """removes previous recv_msg without removing local branch stub, 
        use for cases were a Customer has more than one set of events to perform."""
        self.recvMsg = list()

    def createStubs(self, branch_metadata_list : list[branch_input]) -> list[branch_client_stub]:                 # pylint: disable=invalid-name
        """Creates an object with the branch metadata and stub pointer"""
        return_list: list[branch_client_stub] = []
        for branch_metadata in branch_metadata_list:
            channel = grpc.insecure_channel(f'localhost:{branch_metadata.port}')
            stub = branch_pb2_grpc.branchEventSenderStub(channel)
            return_list.append(branch_client_stub(branch_metadata, stub))
        return return_list

    def find_stub(self, dest_id:int) -> branch_client_stub:
        """Finds the correct stub based on incoming dest id"""
        for stub in self.stub_list:
            if stub.branch_metadata.id == dest_id:
                return stub


    def executeEvents(self,events: list[event]):                                                # pylint: disable=invalid-name
        """Execute events from a customer. This is not all events for that customer, 
        just a subset that occurs at the same time"""


        for incoming_event in events:
            while True:
                response: branchEventResponse = self.find_stub(incoming_event.dest).branch_stub.MsgDelivery(
                    request = branchEventRequest(
                        customer_id=self.id,
                        event_id=incoming_event.id,
                        event_type= incoming_event.interface.name,
                        money= incoming_event.money,
                        is_propogate=False))
                if response.write_id >= self.last_write_id:
                    self.last_write_id = response.write_id
                    break

            if response.event_type ==  branch_pb2.event_type_enum.QUERY:                        # pylint:disable=no-member
                self.recvMsg.append(event_query_response("query", response.balance))

            elif response.event_type ==  branch_pb2.event_type_enum.DEPOSIT:                    # pylint:disable=no-member
                success_str : str
                if response.is_success is True:
                    success_str = "success"
                else:
                    success_str = "failed"

                self.recvMsg.append(event_mutate_response("deposit", success_str))

            elif response.event_type ==  branch_pb2.event_type_enum.WITHDRAW:                   # pylint:disable=no-member
                success_str : str
                if response.is_success is True:
                    success_str = "success"
                else:
                    success_str = "failed"

                self.recvMsg.append(event_mutate_response("withdraw", success_str))
            else:
                raise ValueError("Encountered an unexpected event_type")

    def get_customer_log(self) -> customer_response:
        "create a custom response object for output"
        return_list = []
        for eventMessage in self.recvMsg:
            if eventMessage.interface == "query":
                return_list.append(eventMessage)
                
        return customer_response(self.id, return_list)
