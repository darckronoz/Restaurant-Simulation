from enum import Enum

#Tipos de pago
class QueueStateEnum (Enum):
    Vacio = 0
    En_Cola = 1
    Proceso = 2
    Finalizado=3