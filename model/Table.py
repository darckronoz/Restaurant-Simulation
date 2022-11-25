import numpy as np

from Customer import Customer
from CustomerGroup import CustomerGroup


class Table:

    capacity = 5
    customersGroupList = []

    #customers: array of customers.
    def __init__(self, state, table_id):
        self.state = state
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
        if self.isEmpty:
            self.customersGroupList.append(customGroup)
            self.customersGroupList = np.array(self.customersGroupList)
            print(self.customersGroupList[0].customer[0].customer_id)
            self.capacity -= len(self.customersGroupList[0].customer)
        elif self.setShareable and self.customersGroupList.size <2 and self.capacity >=len(customGroup.customer):
            self.customersGroupList = np.concatenate((self.customersGroupList, customGroup))
            self.capacity -= self.customersGroupList[1].customer.size


    #function that returns True if the customers array is empty
    def isEmpty(self):
        return len(self.customersGroupList) == 0

    #TO DO:
    #when there is an even number of customers on the table 
    #and half say yes and the other half say no to share the table,
    #the restaurant will prioritize to share the table.

    #this function gets the share parameter for each customer 
    #then if the majority agrees to share then returns true
    #if the majority agrees not to share returns false
    #if it is even returns true.
    def setShareable(self):
        trueCounter = 0
        for i in range(self.customersGroupList[0].customer.size):
            if self.customersGroupList[i]._share_table:
                trueCounter += 1
            falses=self.customersGroupList.size-trueCounter
            if trueCounter>=falses:
                return True
            return False

    def show(self):
        var=""
        for i in range(self.customersGroupList.size):
            for n in self.customersGroupList[i].customer:
                print('id:', n.customer_id)
        return var

