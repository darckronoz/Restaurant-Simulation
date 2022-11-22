import numpy as np


class CustomerGroup:
    
    #customers: array of customers (max lenght 5)
    #eating_time: pending.
    def __init__(self, customers, eating_time):
        self.customers = customers
        self.eating_time = eating_time

    #this function returns the size of the group
    def getSize(self):
        return len(self.customers)
        





    

