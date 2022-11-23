import numpy as np
class Table:

    capacity = 5
    shareable = False
    customers = np.array

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
    def addCustomer(self, customers):
        if self.isEmpty:
            self.customers = np.array(customers)
            self.capacity -= len(customers)
            self.setShareable()
        else:
            self.customers = np.concatenate((self.customers, customers))
            self.capacity -= len(customers)
            self.shareable = False


    #function that returns True if the customers array is empty
    def isEmpty(self):
        if len(self.customers) <= 0:
            return True
        return False

    #TO DO:
    #when there is an even number of customers on the table 
    #and half say yes and the other half say no to share the table,
    #the restaurant will prioritize to share the table.

    #this function gets the share parameter for each customer 
    #then if the majority agrees to share then returns true
    #if the majority agrees not to share returns false
    #if it is even returns true.
    def setShareable(self):
        n = len(self.customers)
        trueCounter = 0
        for customer in self.customers:
            if customer.share_table:
                trueCounter += 1
        if n == 2 or n == 4:
                if trueCounter >= n/2:
                    return True
        else:
            if trueCounter > n/2:
                return True
        return False

    def mostrar(self):
        return self.customers




