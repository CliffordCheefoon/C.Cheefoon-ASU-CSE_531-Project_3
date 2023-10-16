import logging
from services.gprc_coms import branch_pb2_grpc
from services.input_parser.parser import branch_input



class Branch(branch_pb2_grpc.branchEventSenderServicer):
    """Handler Class for the grpc server"""

    def __init__(
            self,
            branch_data:branch_input,
            branches_inputs: list[branch_input],
            server_log_dir: str):
        # unique ID of the Branch
        self.id = branch_data.id
        # replica of the Branch's balance
        self.balance = branch_data.balance
        # the list of process IDs of the branches
        #self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.stub_list = list()
        # a list of received messages used for debugging purpose
        self.recv_msg = list()
        # iterate the processID of the branches
        self.branch_cluster_info : list[branch_input]  = branches_inputs

        # TODO: students are expected to store the processID of the branches
        server_log_dir = server_log_dir + f"/server-{self.id}.txt"
        logging.basicConfig(filename=server_log_dir,
                    filemode='w',
                    format='%(asctime)s.%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
        logging.debug(f"Branch server ID:{self.id} started on port: {branch_data.port}")
        logging.debug(f"Starting balance: ${self.balance}")        

    # TODO: students are expected to process requests from both Client and Branch
    def MsgDelivery(self,request, context):
        pass
