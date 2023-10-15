

import decimal
import logging
from enum import Enum

class customer_input_interface_enum(Enum):
    DEPOSIT = 1
    WITHDRAW = 2
    QUERY = 3

class event:
    id : int
    interface : customer_input_interface_enum
    money : decimal
    def __init__(self, id: int, interface: customer_input_interface_enum, money: decimal = None):
        self.id = id
        self.interface = interface
        self.money = money

class customer_input:
    id : int
    events: list[event]

    def __init__(self, id:int , events: list[event]):
        self.id = id
        self.events = events

class branch_input:
    id : int
    balance: decimal


    def __init__(self, id:int , balance: decimal):
        self.id = id
        self.balance = balance



def get_branches(input_obj, logger : logging.Logger) -> list[branch_input]:
    input_branches : list[branch_input]  = []

    for obj in input_obj:
        if obj["type"] == "branch":
            logger.debug(f"""found branch-> id:{obj["id"]}, balance:{obj["balance"]} """)
            input_branches.append(branch_input(obj["id"],obj["balance"]))

    return input_branches


def get_customers(input_obj, logger : logging.Logger) -> list[customer_input]:
    input_customers : list[customer_input]  = []

    for obj in input_obj:
        if obj["type"] == "customer":
            events : list[event] = []

            for event_input in  obj["events"]:

                event_interface: customer_input_interface_enum
                if event_input["interface"] == "withdraw":
                    event_interface = customer_input_interface_enum.WITHDRAW
                elif event_input["interface"] == "query":
                    event_interface = customer_input_interface_enum.QUERY
                elif event_input["interface"] == "deposit":
                    event_interface = customer_input_interface_enum.DEPOSIT
                else:
                    raise ValueError(f"""An unexpected customer event interface was encountered: {event["interface"]}""")

                logger.debug(f"""found customer event-> customer_id:{obj["id"]}, event_id:{event_input["id"]}, event_interface: {event_input["interface"]}, event_money: {event_input.get("money")} """)
                events.append(event(event_input["id"],event_interface, event_input.get("money")))

            input_customers.append(customer_input(obj["id"], events))
    return input_customers