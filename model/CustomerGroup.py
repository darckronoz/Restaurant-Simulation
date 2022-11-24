
from model.PaymentModeEnum import PaymentModeEnum
from model.PaymentTypeEnum import PaymentTypeEnum


class CustomerGroup:
    
    #customers: array of customers (max lenght 5)
    #eating_time: pending.
    def __init__(self, customers, paymentType, paymentMode):
        self._customers =customers
        self._paymentType=PaymentTypeEnum(paymentType)
        self._paymentMode=PaymentModeEnum(paymentMode)

    def _get_customer(self):
        return self._customers

    def _get_paymentType(self):
        return self._paymentType

    def _get_paymentMode(self):
        return self._paymentMode

    def _service_time(self):
        return "Fabuchitor"




    customer=property(fget=_get_customer)
    paymentType=property(fget=_get_paymentType)
    paymentMode=property(fget=_get_paymentMode)
    serviceTime=property(fget=_service_time)


# r=CustomerGroup("fe","sef","sf")
# print(r.serviceTime)
# print(r.customer)





    

