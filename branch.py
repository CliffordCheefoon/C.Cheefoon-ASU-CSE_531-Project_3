from services.gprc_coms import branch_pb2
from services.gprc_coms import branch_pb2_grpc
import logging 



class Branch(branch_pb2_grpc.branchEventSenderServicer):

    def __init__(self, id, balance, branches, server_log_dir: str, server_port: int):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.stubList = list()
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # iterate the processID of the branches

        # TODO: students are expected to store the processID of the branches
        server_log_dir = server_log_dir + f"/server-{self.id}.txt"
        logging.basicConfig(filename=server_log_dir,
                    filemode='w',
                    format='%(asctime)s.%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
        logging.debug(f"Branch server ID:{self.id} started on port: {server_port}")
        logging.debug(f"Starting balance: ${self.balance}")
        
        pass

    # TODO: students are expected to process requests from both Client and Branch
    def MsgDelivery(self,request, context):
        pass



    
