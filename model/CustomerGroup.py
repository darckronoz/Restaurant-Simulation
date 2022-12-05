
from PaymentModeEnum import PaymentModeEnum
from PaymentTypeEnum import PaymentTypeEnum


class CustomerGroup:
    
    #customers: array of customers (max lenght 5)
    #eating_time: pending.
    def __init__(self, id_group, customers, paymentType, paymentMode):
        self._id_group = id_group
        self._customers = customers
        self._paymentType = PaymentTypeEnum(paymentType)
        self._paymentMode = PaymentModeEnum(paymentMode)
        self._total_price_orderGroup = 0
        # self._total_time_orderGroup = 0
        self._eat_process_finish = False

    def _get_customer(self):
        return self._customers

    def _get_id_group(self):
        return self._id_group

    def _get_paymentType(self):
        return self._paymentType

    def _get_paymentMode(self):
        return self._paymentMode

    def _set_eat_process_finish(self, eatFinish):
        self._eat_process_finish=eatFinish

    def _get_eat_process_finish(self):
        return self._eat_process_finish


    # Tiempo total de grupo por mesa
    def totalTimeServiceGroup(self):
        total_time_orderGroup=0
        d=[]
        for i in range(len(self._customers)):
            d.append(self.customer[i].order.get_total_time())
            total_time_orderGroup=max(d)
        return total_time_orderGroup


    # Precio total de grupo
    def _get_total_price_order_group(self):
        for i in range(len(self._customers)):
            self._total_price_orderGroup+=self._customers[i].order.get_total_order()
        return self._total_price_orderGroup



    customer=property(fget=_get_customer)
    idGroup= property(fget=_get_id_group)
    paymentType=property(fget=_get_paymentType)
    paymentMode=property(fget=_get_paymentMode)
    eatProcess=property(fget=_get_eat_process_finish, fset=_set_eat_process_finish)
    totalPriceGroup=property(fget=_get_total_price_order_group)


# r=CustomerGroup("fe","sef","sf")
# print(r.serviceTime)
# print(r.customer)





    

