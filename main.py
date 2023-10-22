import json
import logging
import time
from customer import Customer
from services.input_parser.parser import get_branches, get_customers
from services.server_spawner.manager import branch_server_spawn_manager


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
PORT_OFFSET : int = 50000
TEST_INPUT : str = """tests/test_case.json"""
BRANCH_SERVER_LOG_DIR :str = """tests/server_out/"""


def main(input_file_dir : str):
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

    for branch in branches_inputs:
        Customers.append(Customer(branch.id, branch))

    for customer_input in customer_inputs:
        for customer in Customers:
            if customer_input.id == customer.id:
                customer.executeEvents(customer_input.events)


    #branch_server_spawn_manager_instance.terminate_servers()


if __name__ == "__main__":
    main(TEST_INPUT)
