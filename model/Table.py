import threading



class Table:

    def __init__(self, table_id):
        self.is_on = True
        self.table_capacity = 5
        self.customersGroupList = []
        self.state = True
        self.table_id = table_id
        self.customersQueue = []
        self.customer_finished = None

    def addCustomer(self, customGroup):
        if self.isEmpty():
            self.customersGroupList.append(customGroup)
            print(self.customersGroupList[0].customer[0].customer_id)
            self.table_capacity -= len(self.customersGroupList[0].customer)
            return True
        elif self.tableAvailable() and self.table_capacity >= len(customGroup.customer):
            self.customersGroupList.append(customGroup)
            self.table_capacity -= len(self.customersGroupList[1].customer)
            return True
        return False

    def isEmpty(self):
        return len(self.customersGroupList) == 0

    def addOrder(self, order):
        for n in self.customersGroupList[0].customer:
            n.order = order

    def setShareable(self):
        trueCounter = 0
        for i in range(len(self.customersGroupList[0].customer)):
            if self.customersGroupList[0].customer[i]._share_table:
                trueCounter += 1
            falses = len(self.customersGroupList) - trueCounter
            if trueCounter >= falses:
                return True
            return False

    def get_table_id(self):
        return self.table_id

    # Ver disponibilidad de la mesa
    def tableAvailable(self):
        return len(self.customersGroupList) < 2 and self.setShareable()

    def get_customer_queue(self):
        return self.customersQueue

    def show(self):
        for i in range(len(self.customersGroupList)):
            print(self.customersGroupList[i].idGroup)
            for n in self.customersGroupList[i].customer:
                print('id:', n.customer_id)

    def get_list(self):
        return self.customersGroupList

    def start_service(self):
        while self.is_on:
            for c in self.customersGroupList:
                if c.eatProcess:
                    self.customer_finished = c
                    # print("Mesa: ", self.table_id, " Grupo:", c.idGroup)
                    self.customersGroupList.remove(c)

    def get_customer_finished(self):
        return self.customer_finished

    def set_customer_finished(self):
        self.customer_finished = None

    def shut_down(self):
        self.is_on= False


    def start(self):
        hiloTableTrue = threading.Thread(target=self.start_service)
        hiloTableTrue.start()
