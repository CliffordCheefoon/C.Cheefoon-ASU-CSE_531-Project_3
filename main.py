import json
import logging
import time
from customer import Customer, customer_response
from services.input_parser.parser import get_branches, get_customers
from services.server_spawner.manager import branch_server_spawn_manager
import os
import glob
import jsonpickle

#######################config####################################
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
PORT_OFFSET : int = 50000
TEST_INPUT_FILE : str = """tests/monotonic_writes.json"""
TEST_OUTPUT_FILE: str = """tests/output/output.json"""
BRANCH_SERVER_LOG_DIR :str = """tests/server_out/"""
################################################################


class final_output:
    """Project 3 specific output fomat"""
    def __init__(self, incoming_id, balance):
        self.id:int = incoming_id
        self.balance = balance

def main(input_file_dir : str):
    #Create directories for output files
    os.makedirs(os.path.dirname(TEST_OUTPUT_FILE), exist_ok=True)
    os.makedirs(os.path.dirname(BRANCH_SERVER_LOG_DIR), exist_ok=True)

    #Clear previous run branch server logs
    files = glob.glob(f'{BRANCH_SERVER_LOG_DIR}*')
    for f in files:
        os.remove(f)

    input_json = json.load( open(input_file_dir, 'r', encoding="UTF8"))
    branches_inputs = get_branches(input_json, logging.getLogger())
    customer_inputs = get_customers(input_json, logging.getLogger())
    branch_server_spawn_manager_instance = branch_server_spawn_manager()
    branch_server_spawn_manager_instance.assign_ports(branches_inputs, PORT_OFFSET)
    for branches_input in branches_inputs:
        branch_server_spawn_manager_instance.spawn_server(
            branches_input, branches_inputs, BRANCH_SERVER_LOG_DIR )

    time.sleep(2)

    Customers : list[Customer] = []

    for customer in customer_inputs:
        Customers.append(Customer(customer.id, branches_inputs))

    with open(TEST_OUTPUT_FILE, "w", encoding="UTF8") as outfile:
        customer_output : list = []
        for customer_input in customer_inputs:
            for customer in Customers:
                if customer_input.id == customer.id:
                    customer.soft_reset()
                    customer.executeEvents(customer_input.events)
                    customer_output.append(customer.get_customer_log())
                    break


        final_output_list: list[final_output] = []
        for output in customer_output:
            final_output_list.append(final_output(output.id, output.recv[0].balance))

        outfile.write(jsonpickle.encode(final_output_list,  unpicklable=False) + "\n")


    branch_server_spawn_manager_instance.terminate_servers()


if __name__ == "__main__":
    main(TEST_INPUT_FILE)
