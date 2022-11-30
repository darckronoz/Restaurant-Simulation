from model.QueueStateEnum import QueueStateEnum
import threading
import datetime
import time


class Cashier:

    def __init__(self):
        self._state = False
        self._clientGroupQueue = []
        self._totalPay = 0

    # Orden pago
    def payProcess(self):

        while True:
            print(len(self._clientGroupQueue))
            if len(self._clientGroupQueue) != 0:
                self._state = True
                time.sleep(5)
                self.totalPay()
                self.popClientGroupQueue()


    # Se agrega a la cola de pagos
    def addClientGropQueue(self, clientGropQueue):
        self._clientGroupQueue.append(clientGropQueue)

    # Se borra el primero de la fila
    def popClientGroupQueue(self):
        self._clientGroupQueue.pop(0)

    def payBill(self):
        return self._clientGroupQueue[0].totalPriceGroup

    def totalPay(self):
        self._totalPay += self.payBill()
        print("Total ", self._totalPay)

    def start(self):
        self._hilo1 = threading.Thread(target=self.payProcess)
        self._hilo1.start()

    # def showCashier(self):
    #     for i in range (len(self._clientGroupQueue)):
    # print(self._clientGroupQueue[i])
