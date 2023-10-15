
from concurrent import futures
from branch import Branch
from services.gprc_coms import branch_pb2
from services.gprc_coms import branch_pb2_grpc
from services.input_parser.parser import branch_input
from multiprocessing import Process
import grpc


def serve(PORT_OFFSET : int , branch_data:  branch_input, server_log_dir :str):
    port = str(PORT_OFFSET + branch_data.id)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    branch_pb2_grpc.add_branchEventSenderServicer_to_server(Branch(branch_data.id, branch_data.balance, None, server_log_dir, port ), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    server.wait_for_termination()


class server_spawn_manager():

    def  __init__(self):
        self.server_processes: list[Process] = []



    def spawn_server(self, PORT_OFFSET : int , branch_data:  branch_input, server_log_dir :str):
        p = Process(target=serve, args=(PORT_OFFSET, branch_data,server_log_dir))
        p.start()
        self.server_processes.append(p)
        
  

    def terminate_all(self):
        for process in self.server_processes:
            process.terminate()

