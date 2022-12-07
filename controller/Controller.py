# imports.
import threading
import time
import random as ran

from distributed import get_task_stream

# import Utilities.
from model.PlateTypeEnum import PlateTypeEnum
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
        self.is_paying = True
        self.attend = True
        self.hiloo = None
        self.hiloprincipal = None
        self.plateList = []
        self.mesasList = []
        self.customerGroupList = []
        self.idGroup = 0
        self.idOrder = 0
        self.create_plates()
        self.create_tables()
        self.cashier = Cashier()
        self.finalList = []

    def create_plates(self):
        plate = Plate(1, "Churrasco", 1, 80, 3, 1)
        plateTwo = Plate(2, "Bistec a Caballo", 1, 2, 10, 2)
        plateThree = Plate(3, "Frijoles con Cayo", 5, 23, 2, 1)
        self.plateList.append(plate)
        self.plateList.append(plateTwo)
        self.plateList.append(plateThree)

    def create_group(self):
        list = []
        for i in range(ran.randint(1, 5)):
            tip = ran.randint(0, 1)
            if tip == 1:
                tip = True
                share = False
            else:
                tip = False
                share = True
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

    def start(self, t):
        self.hiloo = threading.Thread(target=self.paying)
        self.hiloprincipal = threading.Thread(target=self.start_simuation, args=(t,))
        self.hiloo.start()
        self.hiloprincipal.start()
        self.cashier.start()

    def paying(self):
        while self.is_paying:
            for i in self.mesasList:
                if i.get_customer_finished() is not None:
                    self.cashier.addClientGropQueue(i.get_customer_finished())
                    i.set_customer_finished()

    def start_attend_people(self):
        while self.attend:
            tiempo = ran.randint(1, 5)
            time.sleep(tiempo)
            self.add_group_to_table()

    def start_simuation(self, t):
        while t:
            time.sleep(1)
            t -= 1
            print("Quedan:   ", t)
        self.attend = False
        self.is_paying = False
        self.cashier.shutdown()
        self.shut_down_tables()
        self.finalList = self.cashier.get_queue()
        print("-------------------La simulación finalizó----------")
        print("Total: ", self.cashier.get_total())
        for i in self.most_score_plates_name(PlateTypeEnum.Fuerte):
            print(i)
        for i in self.most_score_plates(PlateTypeEnum.Fuerte):
            print(i)
        time.sleep(5)
        # plt.bar(["aaa"], [1])
        # plt.title("Grafico platos fuertes")
        # plt.show()

    def most_score_plates(self, type_plate):
        d = []
        for i in self.plateList:
            if i.plateType == type_plate:
                d.append(round(i.score, 1))
            return d

    def most_score_plates_name(self, type_plate):
        d = []
        for i in self.plateList:
            if i.plateType == type_plate:
                d.append(i.name)
            return d

    def shut_down_tables(self):
        for i in self.mesasList:
            i.shut_down()


c = Controller()
c.start(40)
c.init_thread_table()
c.start_attend_people()
