import json
import logging
from services.input_parser.parser import get_branches, get_customers




def main(input_file_dir : str):
    input  = json.load( open(input_file_dir, 'r') ) 
    branches_inputs = get_branches(input, logging.getLogger())
    customer_inputs = get_customers(input, logging.getLogger())

    


    

if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    main("tests\sample1_input.json")