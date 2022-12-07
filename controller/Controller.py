# imports.
import threading
import time
import random as ran

from distributed import get_task_stream

# import Utilities.

from utilities.Utilities import *

from model.Cashier import Cashier
from model.Chef import Chef
from model.Customer import Customer
from model.CustomerGroup import CustomerGroup
from model.Kitchen import Kitchen
from model.Table import Table
from model.Waiter import Waiter
from model.Order import Order
from model.Plate import Plate


# init restaurant
# restaurant waiting queue. [ ]
# create objects. [x]
# 1 Cashier [x]
# 3 Chefs [x]
# 1 Kitchen [x]
# 4 Waiters [x]
# 20 Tables [x]


# TO:DO Restaurant entry queue
restaurant_queue = []

class Controller:

    def __init__(self):
        # self.initTodo()
        self.plateList = []
        self.mesasList = []
        self.customerGroupList = []
        self.idGroup = 0
        self.idOrder = 0
        self.create_plates()
        self.create_tables()
        # self.create_cashier()
        self.cashier = Cashier()

    def create_plates(self):
        plate = Plate(1, "Churrasco", 1, 15, 80, 3, 1)
        plateTwo = Plate(2, "Bistec a Caballo", 1, 10, 2, 10, 2)
        plateThree = Plate(3, "Frijoles con Cayo", 5, 23, 2, 2, 1)
        self.plateList.append(plate)
        self.plateList.append(plateTwo)
        self.plateList.append(plateThree)

    def create_group(self):
        list = []
        for i in range(ran.randint(1, 5)):
            tip = ran.randint(0, 1)
            share = 0
            if tip == 1:
                tip = True
                share = False
            else:
                tip = False
                share = True
            # print(tip)
            customer = Customer(ran.randint(1, 1000), tip, ran.randint(1, 4), share)
            list.append(customer)
        self.idGroup += 1
        customerG = CustomerGroup(self.idGroup, list, ran.randint(1, 3), ran.randint(1, 3))
        return customerG

    def create_orders(self, plateList):
        self.idOrder += 1
        order = Order(self.idOrder, plateList)
        return order

    def create_tables(self):
        for i in range(20):
            self.mesasList.append(Table(i + 1))

    def add_group_to_table(self):
        customerG = self.create_group()
        for i in range(len(self.mesasList)):
            if self.mesasList[i].addCustomer(customerG):
                print('Se añadío a la mesa ', self.mesasList[i].get_table_id())
                self.addOrder(customerG)
                customerG.totalTimeServiceGroup()
                customerG.start()
                break
            else:
                print("Sin disponibilidad en la mesa: ", self.mesasList[i].get_table_id())

    def addOrder(self, customerG):
        for customer in customerG.customer:
            customer.order = self.create_orders(self.assign_order_to_customer(customer.capacity))

    def assign_order_to_customer(self, capacidad):
        list = []
        for i in range(ran.randint(1, capacidad)):
            list.append(self.plateList[ran.randint(1, len(self.plateList) - 1)])
        return list

    # cashier.totalPay()

    # def show(self):
    #     # Muestra informacion
    #     for i in range(len(customerGroup.customer)):
    #         print(customerGroup.customer[i].customer_id)
    #         for j in range(len(customerGroup.customer[i].order.plates)):
    #             print(customerGroup.customer[i].order.plates[j].name)
    #             print("EL tiempo total gastado por grupo es  ", customerGroup.totalTimeServiceGroup())

    def create_cashier(self):
        pass

    def init_thread_table(self):
        # activa los hilos de todas las mesas
        for i in self.mesasList:
            i.start()

    def get_list_queue(self):
        while True:
            d = []
            if len(self.mesasList[0].get_customer_queue()) > 0:
                d.append(self.mesasList[0].get_customer_queue()[0])
                print("ID:  ", d[0].idGroup)

    def start(self):
        # hiloo = threading.Thread(target=self.get_list_queue)
        # hiloo.start()
        hiloo = threading.Thread(target=self.paying)
        hiloo.start()
        self.cashier.start()

    def paying(self):
        while True:
            for i in self.mesasList:
                if i.get_customer_finished() is not None:
                    self.cashier.addClientGropQueue(i.get_customer_finished())
                    i.set_customer_finished()


c = Controller()
c.add_group_to_table()
c.add_group_to_table()
c.add_group_to_table()
c.add_group_to_table()

c.init_thread_table()
c.start()

# def initTodo(self):
#             #chefs.
#     margin_error_chef = [0, 0, 0] #fill with the function margin error in Utilities
#     plates_chef_one = []
#     chefOne = Chef(1, plates_chef_one, None, margin_error_chef[0], False)
#     plates_chef_two = []
#     chefTwo = Chef(1, plates_chef_two, None, margin_error_chef[1], False)
#     plates_chef_three = []
#     chefThree = Chef(1, plates_chef_three, None, margin_error_chef[2], False)
#
#     #kitchen.
#     chefs = [chefOne, chefTwo, chefThree]
#     freezer = [] #queue
#     kitchen = Kitchen(chefs, freezer)
#
#     #tables.
#     tables = []
#     for i in range(20):
#         tables.append(Table(False, i+1))
#
#     #waiters.
#     waiters = []
#     orderTimes = [0, 0, 0, 0]
#     cleanTimes = [0, 0, 0, 0]
#     serviceTimes = [0, 0, 0, 0]
#     for i in range(4):
#         waiters.append(Waiter(i+1, False, orderTimes[i], cleanTimes[i], serviceTimes[i], tables, 0, 0))

