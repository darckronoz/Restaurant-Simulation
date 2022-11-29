from model.QueueStateEnum import QueueStateEnum


class Cashier:

    def __init__(self):
        self._state= QueueStateEnum(0)
        self._clientGroupQueue = []
        self._totalPay=0



    # Se agrega a la cola de pagos
    def addClientGropQueue(self, clientGropQueue):
        self._clientGroupQueue.append(clientGropQueue)

    # Se borra el primero de la fila
    def popClientGroupQueue(self):
        self._clientGroupQueue.pop(0)

    def payBill(self):
        return self._clientGroupQueue[0].totalPriceGroup


    def totalPay(self):
        self._totalPay+=self.payBill()
        print("Total ", self._totalPay)

    # def showCashier(self):
    #     for i in range (len(self._clientGroupQueue)):
           # print(self._clientGroupQueue[i])




