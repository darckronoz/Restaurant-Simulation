from enum import Enum

#Estados en cola
class QueueStateEnum (Enum):
    Vacio = 0
    En_Cola = 1
    Proceso = 2
    Finalizado=3