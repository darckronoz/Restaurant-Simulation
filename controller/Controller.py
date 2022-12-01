#imports.

import random as r

from model.Cashier import Cashier
from model.Chef import Chef
from model.Customer import Customer
from model.CustomerGroup import CustomerGroup
from model.Kitchen import Kitchen
#from model.Order import Order
#from model.Plate import Plate
from model.Table import Table
from model.Waiter import Waiter

#import Utilities.

from utilities.Utilities import *

#init restaurant
#restaurant waiting queue. [ ]
#create objects. [x]
#1 Cashier [x]
#3 Chefs [x]
#1 Kitchen [x]
#4 Waiters [x]
#20 Tables [x]
cashier_queue = []
cashier = Cashier()

#chefs.
margin_error_chef = [0, 0, 0] #fill with the function margin error in Utilities
plates_chef_one = []
chefOne = Chef(1, plates_chef_one, None, margin_error_chef[0], False)
plates_chef_two = []
chefTwo = Chef(1, plates_chef_two, None, margin_error_chef[1], False)
plates_chef_three = []
chefThree = Chef(1, plates_chef_three, None, margin_error_chef[2], False)

#kitchen.
chefs = [chefOne, chefTwo, chefThree]
freezer = [] #queue
kitchen = Kitchen(chefs, freezer)

#tables.
tables = []
for i in range(20):
    tables.append(Table(False, i+1))

#waiters.
waiters = []
orderTimes = [0, 0, 0, 0]
cleanTimes = [0, 0, 0, 0]
serviceTimes = [0, 0, 0, 0]
for i in range(4):
    waiters.append(Waiter(i+1, False, orderTimes[i], cleanTimes[i], serviceTimes[i], tables, 0, 0))


# <-provisional customer group creation.
customer_number = r.randint(1, 5)
customers = []
for i in range(customer_number):
    customers.append(Customer(i, False, 3, True))
group = CustomerGroup(customers, r.randint(1, 3), r.randint(1, 3))
# end provisional customer group creation.->

# customer arrives
# TO DO: Arrival customer distribution *Utilities*

# def customer_arrives():
# TO DO
# queue of task for the waiter
#








