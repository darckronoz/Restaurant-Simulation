import numpy as np

from Customer import Customer
from CustomerGroup import CustomerGroup

from model.Order import Order


class Table:

    capacity = 5

    #customers: array of customers.
    def __init__(self, table_id):
        self.customersGroupList = []
        self.state = True
        self.table_id = table_id

    #the restaurant only admits to share the table once
    #if the table is empty the customers will be the new self.customers array
    #the capacity will be 5 - (the lenght of the customers array)
    #and it'll call setShareable function with the new customers

    #if it's a call to share the table it has to had completed the conditions on Waiter Class
    #so it'll only enter the else if the group is smaller or equal to the table capacity
    #and if the table is shareable
    #then it'll concatenate the self.customers array with the array to share with
    #update the capacity and set Shareable to False so it cant be shared again.
    def addCustomer(self, customGroup):
        if self.isEmpty():
            self.customersGroupList.append(customGroup)
            print(self.customersGroupList[0].customer[0].customer_id)
            self.capacity -= len(self.customersGroupList[0].customer)
            return True
        elif self.tableAvailable() and self.capacity >=len(customGroup.customer):
            self.customersGroupList.append(customGroup)
            self.capacity -= len(self.customersGroupList[1].customer)
            return True
        return False


    #function that returns True if the customers array is empty
    def isEmpty(self):
        return len(self.customersGroupList) == 0

    def addOrder(self, order):
        for n in self.customersGroupList[0].customer:
            n.order=order

    def setShareable(self):
        trueCounter = 0
        for i in range(len(self.customersGroupList[0].customer)):
            if self.customersGroupList[0].customer[i]._share_table:
                trueCounter += 1
            falses=len(self.customersGroupList)-trueCounter
            if trueCounter>=falses:
                return True
            return False

    def get_table_id(self):
        return self.table_id

    # Ver disponibilidad de la mesa
    def tableAvailable(self):
        return len(self.customersGroupList) < 2 and self.setShareable()



    def show(self):
        for i in range(len(self.customersGroupList)):
            print(self.customersGroupList[i].idGroup)
            for n in self.customersGroupList[i].customer:
                print('id:', n.customer_id)


