import threading
import time
import random as ran
from model.PaymentModeEnum import PaymentModeEnum
from model.PaymentTypeEnum import PaymentTypeEnum


class CustomerGroup:

    # customers: array of customers (max lenght 5)
    # eating_time: pending.
    def __init__(self, id_group, customers, paymentType, paymentMode):
        self._id_group = id_group
        self.customer_list = customers
        self._paymentType = PaymentTypeEnum(paymentType)
        self._paymentMode = PaymentModeEnum(paymentMode)
        self._total_price_orderGroup = 0
        self.total_time_orderGroup = 0
        self._eat_process_finish = False

    def _get_customer_list(self):
        return self.customer_list

    def _get_id_group(self):
        return self._id_group

    def _get_paymentType(self):
        return self._paymentType

    def _get_paymentMode(self):
        return self._paymentMode

    def _set_eat_process_finish(self, eatFinish):
        self._eat_process_finish = eatFinish

    def _get_eat_process_finish(self):
        return self._eat_process_finish

    # Tiempo total de grupo por mesa
    def totalTimeServiceGroup(self):
        d = []
        for i in range(len(self.customer_list)):
            d.append(self.customer_list[i].order.get_total_time())
            self.total_time_orderGroup = max(d)
        return self.total_time_orderGroup

    # Precio total de grupo
    def _get_total_price_order_group(self):
        for i in range(len(self.customer_list)):
            self._total_price_orderGroup += self.customer_list[i].order.get_total_order()
        return self._total_price_orderGroup

    def start_eating(self):
        flag = True
        while flag:
            time.sleep(self.total_time_orderGroup)
            self.total_time_orderGroup = 0
            flag = False
            self._eat_process_finish = True
            for i in self.customer:
                for j in i.order.plates:
                    j.score = ran.randint(1, 5)

    def start(self):
        hilo = threading.Thread(target=self.start_eating)
        hilo.start()

    customer = property(fget=_get_customer_list)
    idGroup = property(fget=_get_id_group)
    paymentType = property(fget=_get_paymentType)
    paymentMode = property(fget=_get_paymentMode)
    eatProcess = property(fget=_get_eat_process_finish, fset=_set_eat_process_finish)
    totalPriceGroup = property(fget=_get_total_price_order_group)
