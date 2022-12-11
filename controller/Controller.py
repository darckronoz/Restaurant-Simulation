import ctypes
import multiprocessing
import sys
import threading
import time

from model.PlateTypeEnum import PlateTypeEnum
from utilities.Utilities import *

from model.Cashier import Cashier
from model.Customer import Customer
from model.CustomerGroup import CustomerGroup
from model.Table import Table
from model.Waiter import Waiter
from model.Order import Order
from model.Plate import Plate


class Controller:

    def __init__(self):

        # Tiempos de servicio
        self.order_time = 0.021
        self.clean_time = 0.062
        self.pay_cash = 0.0361
        self.pay_card = 0.0172
        self.pay_bank = 0.0308

        # InitRestaurant
        self.available_tables = 20
        self.restaurant_queue = []
        self.customer_ri = generate_big_ri(10000)
        self.plate_List = []
        self.table_List = []
        self.customer_Group_List = []
        self.waiter_list = []
        self.final_List = []
        self.group_id = 0
        self.order_id = 0
        self.customer_id = 0
        self.create_plates()
        self.create_tables()
        self.cashier = Cashier()
        self.create_waiters()

        # flags & threads
        self.days = multiprocessing.Value(ctypes.c_int, 0)
        self.hours = multiprocessing.Value(ctypes.c_int, 0)
        self.is_paying = True
        self.attend = True
        self.dist_thread = None
        self.timer_thread = None
        self.payment_thread = None
        self.hiloprincipal = None

    def create_waiters(self):
        self.waiter_list.append(
            Waiter(1, False, self.order_time, self.clean_time, [0.0107, 0.0114, 0.0217, 0.0204], self.table_List, 0, 0))
        self.waiter_list.append(
            Waiter(2, False, self.order_time, self.clean_time, [0.0175, 0.0169, 0.0345, 0.0310], self.table_List, 0, 0))
        self.waiter_list.append(
            Waiter(3, False, self.order_time, self.clean_time, [0.0152, 0.0166, 0.0292, 0.0277], self.table_List, 0, 0))
        self.waiter_list.append(
            Waiter(4, False, self.order_time, self.clean_time, [0.0110, 0.0125, 0.0261, 0.0244], self.table_List, 0, 0))

    def create_plates(self):
        pp = 20000
        # entradas
        self.plate_List.append(Plate(1, 'Mini Hojaldres de salchicha', 0.03, 12000, 0.03, 1))
        self.plate_List.append(Plate(2, 'Palitos de berenjena en salsa agridulce', 0.023, 10000, 0.023, 1))
        self.plate_List.append(Plate(3, 'Brochetas de champiñones y espinacas', 0.022, 16000, 0.022, 1))
        self.plate_List.append(Plate(4, 'Pimenton relleno', 0.033, 15000, 0.033, 1))
        self.plate_List.append(Plate(5, 'Ensalada Cesar', 0.025, 12000, 0.025, 1))
        self.plate_List.append(Plate(6, 'Zupa di pomodoro', 0.033, 18000, 0.033, 1))
        self.plate_List.append(Plate(7, 'Canapes de queso brie y cebolla caramelizada', 0.028, 18000, 0.028, 1))
        # fuerte
        self.plate_List.append(Plate(8, 'Pavo rebanado con duraznos', 0.067, 60000, 0.067, 2))
        self.plate_List.append(Plate(9, 'Jamón glaseado con salsa de miel', 0.075, 80000, 0.075, 2))
        self.plate_List.append(Plate(10, 'Brisket con espárragos y romero', 0.05, 75000, 0.05, 2))
        self.plate_List.append(
            Plate(11, 'Lomo de cerdo envuelto en tocino con salsa de mapple', 0.058, 98000, 0.058, 2))
        self.plate_List.append(Plate(12, 'Medallones de res con setas', 0.042, 45000, 0.042, 2))
        self.plate_List.append(Plate(13, 'Pollo en salsa Bechamel', 0.075, 45000, 0.075, 2))
        self.plate_List.append(Plate(14, 'Pes Quinua', 0.042, 82000, 0.042, 2))
        self.plate_List.append(Plate(15, 'Bondiola de cerdo en cerveza', 0.058, 80000, 0.058, 2))
        self.plate_List.append(Plate(16, 'Salmón all-sciliana', 0.092, 120000, 0.092, 2))
        self.plate_List.append(Plate(17, 'Pollo picata', 0.05, 70000, 0.05, 2))
        self.plate_List.append(Plate(18, 'All Marinera', 0.067, 10000, 0.067, 2))
        # postre
        self.plate_List.append(Plate(19, 'Bocaditos de naranja y albahaca', 0.01, 20000, 0.01, 3))
        self.plate_List.append(Plate(19, 'Financiers con frambuesas', 0.01, 25000, 0.01, 3))
        self.plate_List.append(Plate(20, 'Pudín Danés de manzana', 0.013, 30000, 0.013, 3))
        self.plate_List.append(Plate(19, 'Postre de maracuyá', 0.001, 9500, 0.001, 3))
        self.plate_List.append(Plate(20, 'Tiramisú', 0.025, 25000, 0.025, 3))
        self.plate_List.append(Plate(21, 'Gelatto', 0.017, 28000, 0.017, 3))

    def create_group(self):
        aux_list = []
        for i in range(generate_Ni_min_max(1, 5)):
            self.customer_id += 1
            customer = Customer(self.customer_id, generate_Tip(), generate_custm_capacity(), generate_Share())
            aux_list.append(customer)
        self.group_id += 1
        customerG = CustomerGroup(self.group_id, aux_list, generate_pay_type(), generate_pay_mode())
        return customerG

    # creates tables with its id and zones.
    def create_tables(self):
        for i in range(20):
            if i <= 4:
                self.table_List.append(Table(i + 1, 1))
            if 5 <= i < 10:
                self.table_List.append(Table(i + 1, 2))
            if 10 <= i < 15:
                self.table_List.append(Table(i + 1, 3))
            if 15 <= i < 20:
                self.table_List.append(Table(i + 1, 4))

    def sit_group(self):
        group = self.restaurant_queue.pop(0)
        print(f'llegaron {len(group.customer_list)} clientes!')
        for table in self.table_List:
            if table.addCustomer(group):
                if table.full:
                    self.available_tables -= 1
                self.addOrder(group)
                group.totalTimeServiceGroup()
                group.start()
                return True
        return False

    def customer_arrives(self):
        group = self.create_group()
        self.restaurant_queue.append(group)
        if self.available_tables != 0:
            if self.sit_group():
                return

    def customer_distribution(self):
        print('customer Dist started')
        self.customer_arrives()
        for time_arrive in self.customer_ri:
            if not self.attend:
                return
            self.customer_arrives()
            x = get_arrival_time((3 / 7), time_arrive)
            time.sleep(x / 200)

    def create_orders(self, plateList):
        self.order_id += 1
        order = Order(self.order_id, plateList)
        return order

    def addOrder(self, group):
        for customer in group.customer_list:
            customer.order = self.create_orders(self.assign_order_to_customer(customer.capacity))

    def assign_order_to_customer(self, capacity):
        aux_list = []
        for i in range(generate_Ni_min_max(1, capacity)):
            aux_list.append(self.plate_List[generate_Ni_min_max(1, len(self.plate_List) - 1)])
        return aux_list

    def create_cashier(self):
        pass

    def init_thread_table(self):
        # activa los hilos de todas las mesas
        for table in self.table_List:
            table.start()

    def get_list_queue(self):
        while True:
            d = []
            if len(self.table_List[0].get_customer_queue()) > 0:
                d.append(self.table_List[0].get_customer_queue()[0])
                print("ID:  ", d[0].group_id)

    def start(self):
        self.payment_thread = threading.Thread(target=self.paying)
        self.hiloprincipal = threading.Thread(target=self.start_simulation)
        self.dist_thread = threading.Thread(target=self.customer_distribution)
        self.payment_thread.start()
        self.hiloprincipal.start()
        self.dist_thread.start()
        self.cashier.start()

    def paying(self):
        print('paying started')
        while self.is_paying:
            for i in self.table_List:
                if i.get_customer_finished() is not None:
                    self.cashier.addClientGropQueue(i.get_customer_finished())
                    i.set_customer_finished()

    def start_simulation(self):
        days = 1
        print(f'simulation started: {days} days')
        while self.days.value < days:
            time.sleep(1)
            self.hours.value += 1
            if self.hours.value == 24:
                self.hours.value = 0
                self.days.value += 1
                print(f'día: {self.days.value} terminado')
        print(('d:', self.days.value, 'h:', self.hours.value))
        self.end_simulation()

    def end_simulation(self):
        self.attend = False
        self.is_paying = False
        self.cashier.shutdown()
        self.shut_down_tables()
        self.final_List = self.cashier.get_queue()
        print("----------------La simulación finalizó----------")
        profit_restaurant(self.cashier.get_total())
        for i in self.most_score_plates_name(PlateTypeEnum.Fuerte):
            print(i)
        for i in self.most_score_plates(PlateTypeEnum.Fuerte):
            print(i)
        # plt.bar(["aaa"], [1])
        # plt.title("Grafico platos fuertes")
        # plt.show()

    def most_score_plates(self, type_plate):
        d = []
        for i in self.plate_List:
            if i.plateType == type_plate:
                d.append(round(i.score, 1))
            return d

    def most_score_plates_name(self, type_plate):
        d = []
        for i in self.plate_List:
            if i.plateType == type_plate:
                d.append(i.name)
            return d

    def shut_down_tables(self):
        for i in self.table_List:
            i.shut_down()


c = Controller()
c.start()
c.init_thread_table()
