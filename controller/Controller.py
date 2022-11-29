#imports.

from model.Cashier import Cashier
from model.Chef import Chef
from model.Customer import Customer
from model.CustomerGroup import CustomerGroup
from model.Kitchen import Kitchen
from model.Order import Order
from model.Plate import Plate
from model.Table import Table
from model.Waiter import Waiter

#import Utilities.

from utilities.Utilities import *

#init restaurant
#create objects.
#1 Cashier
#3 Chefs
#1 Kitchen
#4 Waiters
#20 Tables
cashier_queue = []
cashier = Cashier(False, cashier_queue)

#chef One:
#Plates chef One:
plates_chef_one = []
chefOne = Chef(1, plates_chef_one, None, )
freezer = []
chefs = []
kitchen = Kitchen()


