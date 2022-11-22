
class CustomerGroup:
    
    #customers: array of customers (max lenght 5)
    #eating_time: pending.
    def __init__(self, customers, eating_time):
        self.customers = customers
        self.eating_time = eating_time

    #this function returns the size of the group
    def getSize(self):
        return len(self.customers)

    def addCustomer(self, customers):
        if self.isEmpty:
            self.customers = np.array(customers)
            self.capacity -= len(customers)
            self.setShareable()
        else:
            self.customers = np.concatenate((self.customers, customers))
            self.capacity -= len(customers)
            self.shareable = False

        # function that returns True if the customers array is empty

    def isEmpty(self):
        if len(self.customers) <= 0:
            return True
        return False

        # TO DO:
        # when there is an even number of customers on the table
        # and half say yes and the other half say no to share the table,
        # the restaurant will prioritize to share the table.

        # this function gets the share parameter for each customer
        # then if the majority agrees to share then returns true
        # if the majority agrees not to share returns false
        # if it is even returns true.

    def setShareable(self):
        n = len(self.customers)
        trueCounter = 0
        for customer in self.customers:
            if customer.share_table:
                trueCounter += 1
        if n == 2 or n == 4:
            if trueCounter >= n / 2:
                return True
        else:
            if trueCounter > n / 2:
                return True
        return False





    

