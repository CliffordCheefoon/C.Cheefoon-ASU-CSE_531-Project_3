

import grpc
from branch import branch_client_stub
from services.gprc_coms import branch_pb2_grpc
from services.gprc_coms.branch_pb2 import branchEventRequest # pylint: disable=no-name-in-module
from services.input_parser.parser import branch_input, event






class Customer:
    """A customer with it's own GRPC stub to it's own Branch Server"""
    events: list[event]
    def __init__(self, id: int, branch_metadata : branch_input): # pylint: disable=redefined-builtin
        # unique ID of the Customer
        self.id = id
        # a list of received messages used for debugging purpose
        self.recvMsg = list() # pylint: disable=invalid-name
        # pointer for the stub
        self.stub = self.createStub(branch_metadata)

    def createStub(self, branch_metadata : branch_input) -> branch_client_stub: # pylint: disable=invalid-name
        """Creates an object with the branch metadata and stub pointer"""
        channel = grpc.insecure_channel(f'localhost:{branch_metadata.port}')
        stub = branch_pb2_grpc.branchEventSenderStub(channel)
        return branch_client_stub(branch_metadata, stub)


    def executeEvents(self,events: list[event]): # pylint: disable=invalid-name
        """Execute events from a customer. This is not all events for that customer, 
        just a subset that occurs at the same time"""

        for incoming_event in events:
            self.stub.branch_stub.MsgDelivery(
                request = branchEventRequest(
                    customer_id=self.id,
                    event_id=incoming_event.id,
                    event_type= incoming_event.interface.name,
                    money= incoming_event.money))
