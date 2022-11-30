
from PaymentModeEnum import PaymentModeEnum
from PaymentTypeEnum import PaymentTypeEnum


class CustomerGroup:
    
    #customers: array of customers (max lenght 5)
    #eating_time: pending.
    def __init__(self, customers, paymentType, paymentMode):
        self._customers =customers
        self._paymentType=PaymentTypeEnum(paymentType)
        self._paymentMode=PaymentModeEnum(paymentMode)
        self._total_price_orderGroup=0

    def _get_customer(self):
        return self._customers

    def _get_paymentType(self):
        return self._paymentType

    def _get_paymentMode(self):
        return self._paymentMode

    def _service_time(self):
        return "Fabuchitor"

    def _get_total_price_order_group(self):
        for i in range(len(self._customers)):
            self._total_price_orderGroup+=self._customers[i].order.get_total_order()
        return self._total_price_orderGroup



    customer=property(fget=_get_customer)
    paymentType=property(fget=_get_paymentType)
    paymentMode=property(fget=_get_paymentMode)
    serviceTime=property(fget=_service_time)
    totalPriceGroup=property(fget=_get_total_price_order_group)


# r=CustomerGroup("fe","sef","sf")
# print(r.serviceTime)
# print(r.customer)





    

