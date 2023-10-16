import json
import logging
from services.input_parser.parser import get_branches, get_customers
from services.server_spawner.manager import branch_server_spawn_manager
import os




def main(input_file_dir : str):
    input  = json.load( open(input_file_dir, 'r') ) 
    branches_inputs = get_branches(input, logging.getLogger())
    customer_inputs = get_customers(input, logging.getLogger())
    branch_server_spawn_manager_instance = branch_server_spawn_manager()
    for branches_input in branches_inputs:
        branch_server_spawn_manager_instance.spawn_server(PORT_OFFSET, branches_input, BRANCH_SERVER_LOG_DIR )


    
    branch_server_spawn_manager_instance.terminate_all()




    

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    PORT_OFFSET : int = 50000
    BRANCH_SERVER_LOG_DIR :str = """tests/server_out/"""
    main("tests\sample1_input.json")