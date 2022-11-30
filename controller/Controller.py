#imports.

from model.Cashier import Cashier
from model.Chef import Chef
#from model.Customer import Customer
#from model.CustomerGroup import CustomerGroup
from model.Kitchen import Kitchen
#from model.Order import Order
#from model.Plate import Plate
from model.Table import Table
from model.Waiter import Waiter

#import Utilities.

from utilities.Utilities import *

#init restaurant
#create objects. [x]
#1 Cashier [x]
#3 Chefs [x]
#1 Kitchen [x]
#4 Waiters [x]
#20 Tables [x]
cashier_queue = []
cashier = Cashier(False, cashier_queue)

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


