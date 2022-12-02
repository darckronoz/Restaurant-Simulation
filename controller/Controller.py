# imports.

import random as r
import threading as th

from model.Cashier import Cashier
from model.Chef import Chef
from model.Customer import Customer
from model.CustomerGroup import CustomerGroup
from model.Kitchen import Kitchen
# from model.Order import Order
# from model.Plate import Plate
from model.Table import Table
from model.Waiter import Waiter

customer_counter = 0

# import Utilities.

from utilities.Utilities import *

# init restaurant
# restaurant waiting queue. [ ]
# create objects. [x]
# 1 Cashier [x]
# 3 Chefs [x]
# 1 Kitchen [x]
# 4 Waiters [x]
# 20 Tables [x]

# Restaurant entry queue
restaurant_queue = []

# cashier
cashier_queue = []
cashier = Cashier()

# chefs.
margin_error_chef = [0, 0, 0]  # fill with the function margin error in Utilities
plates_chef_one = []
chefOne = Chef(1, plates_chef_one, None, margin_error_chef[0], False)
plates_chef_two = []
chefTwo = Chef(1, plates_chef_two, None, margin_error_chef[1], False)
plates_chef_three = []
chefThree = Chef(1, plates_chef_three, None, margin_error_chef[2], False)

# kitchen.
chefs = [chefOne, chefTwo, chefThree]
freezer = []  # queue
kitchen = Kitchen(chefs, freezer)

# tables.
tables = []
for i in range(20):
    tables.append(Table(False, i + 1))

# waiters.
waiters = []
orderTimes = [0, 0, 0, 0]
cleanTimes = [0, 0, 0, 0]
serviceTimes = [0, 0, 0, 0]
for i in range(4):
    waiters.append(Waiter(i + 1, False, orderTimes[i], cleanTimes[i], serviceTimes[i], tables, 0, 0))


# customer arrives
def create_new_customer_group():
    customer_number = r.randint(1, 5)
    customers = []
    for x in range(customer_number):
        # make function in utilities that gives the tip, the shareable and the capacity
        customer_number += 1
        customers.append(Customer(customer_number, False, 3, True))
    return CustomerGroup(customers, r.randint(1, 3), r.randint(1, 3))


def sit_customer(group):
    for t in tables:
        v = t.addCustomer(group)
        if v:
            return True
    else:
        restaurant_queue.append(group)
        return False

# TO DO: Arrival customer distribution *Utilities*
#customer_arrival = th.Thread(target=customer_arrives)
