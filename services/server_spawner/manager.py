from multiprocessing import Process
from concurrent import futures
import grpc
from branch import Branch
from services.gprc_coms import branch_pb2_grpc
from services.input_parser.parser import branch_input


def serve_branch(
        branch_data:  branch_input,
        branches_inputs: list[branch_input],
        server_log_dir: str
        ):
    """Creates a grpc server, instantiating and wiring up the Branch Class has the handler """
    port = str(branch_data.port)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    branch_pb2_grpc.add_branchEventSenderServicer_to_server(
        Branch(branch_data,  branches_inputs, server_log_dir ), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    server.wait_for_termination()

class branch_server_spawn_manager(): # pylint: disable=invalid-name
    """A wrapper for managing branch server processes"""
    def __init__(self):
        self.server_processes: list[Process] = []

    def assign_ports(self, branches_inputs: list[branch_input], PORT_OFFSET: int ):
        """A helper method to bulk assign ports to the 
        branch server proccesses before process start"""
        for branch_input_data in branches_inputs:
            branch_input_data.port = PORT_OFFSET + branch_input_data.id


    def spawn_server(
            self,
            branch_data:  branch_input,
            branches_inputs: list[branch_input],
            server_log_dir :str):
        """spawns the branch server in the process referenced in the process list"""
        p = Process(target=serve_branch, args=( branch_data, branches_inputs,server_log_dir))
        p.start()
        self.server_processes.append(p)

    def terminate_servers(self):
        """terminate all the branch server processes in the process list"""
        for process in self.server_processes:
            process.terminate()
