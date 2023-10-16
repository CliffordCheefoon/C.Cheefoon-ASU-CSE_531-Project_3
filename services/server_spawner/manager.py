
from concurrent import futures
from branch import Branch
from services.gprc_coms import branch_pb2
from services.gprc_coms import branch_pb2_grpc
from services.input_parser.parser import branch_input
from multiprocessing import Process
import grpc


def serve_branch( branch_data:  branch_input, branches_inputs: list[branch_input] , server_log_dir :str):
    """Creates a grpc server, instantiating and wiring up the Branch Class has the handler """
    port = str(branch_data.port)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    branch_pb2_grpc.add_branchEventSenderServicer_to_server(Branch(branch_data,  branches_inputs, server_log_dir ), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    server.wait_for_termination()


class branch_server_spawn_manager():
    """A wrapper for managing branch server processes"""

    def  __init__(self):
        self.server_processes: list[Process] = []

    def assign_ports(self, branches_inputs: list[branch_input], PORT_OFFSET : int ):
        """A helper method to bulk assign ports to the branch server proccesses before process start"""
        for branch_input in branches_inputs:
            branch_input.port = PORT_OFFSET + branch_input.id


    def spawn_server(self, branch_data:  branch_input, branches_inputs: list[branch_input], server_log_dir :str):
        p = Process(target=serve_branch, args=( branch_data, branches_inputs,server_log_dir))
        p.start()
        self.server_processes.append(p)
        
  

    def terminate_servers(self):
        for process in self.server_processes:
            process.terminate()
            

