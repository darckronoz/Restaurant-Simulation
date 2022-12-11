from enum import Enum


# Tipos de pago
class PaymentTypeEnum(Enum):
    Tarjeta = 1
    Efectivo = 2
    Transaccion = 3
