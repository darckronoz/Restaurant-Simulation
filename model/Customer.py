import numpy as np

class Customer:

    #El cliente cuenta con un Id, Propina, compartir mesa, capacidad, pedido, puntaje del plato y puntaje del mesero

    def __init__(self, customer_id, tip, share_table, capacity, order, plate_score, waiter_score ):
        self.customer_id = customer_id
        self.tip = tip
        self.share_table = share_table
        self.capacity = capacity
        self.order = order
        self.plate_score = plate_score
        self.waiter_score = waiter_score


    def addOrder(self, order):
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



        