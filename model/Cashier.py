import threading
import time


class Cashier:

    def __init__(self):
        self.is_on = True
        self._state = False
        self._clientGroupQueue = []
        self._totalPay = 0
        self.queue = []

    # Orden pago
    def payProcess(self):
        while self.is_on:
            if len(self._clientGroupQueue) != 0:
                self._state = True
                time.sleep(4)
                self.totalPay()
                self.popClientGroupQueue()

    # Se agrega a la cola de pagos
    def addClientGropQueue(self, clientGropQueue):
        self._clientGroupQueue.append(clientGropQueue)
        self.queue.append(clientGropQueue)

    # Se borra el primero de la fila
    def popClientGroupQueue(self):
        self._clientGroupQueue.pop(0)

    def payBill(self):
        return self._clientGroupQueue[0].totalPriceGroup

    def totalPay(self):
        self._totalPay += self.payBill()

    def start(self):
        hilo1 = threading.Thread(target=self.payProcess)
        hilo1.start()

    def most_score_plates(self, type_plate):
        d = []
        for i in self.queue:
            for j in i.customer:
                for k in j.order.plates:
                    if k.plateType == type_plate:
                        d.append(round(k.score, 1))
                        return d

    def most_score_plates_name(self, type_plate):
        d = []
        for i in self.queue:
            for j in i.customer:
                for k in j.order.plates:
                    if k.plateType == type_plate:
                        d.append(k.name)
                        return d

    def get_queue(self):
        return self.queue

    def shutdown(self):
        self.is_on = False

    def get_total(self):
        return self._totalPay


