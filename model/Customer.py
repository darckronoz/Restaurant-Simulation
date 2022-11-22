import numpy as np

class Customer:

    #El cliente cuenta con un Id, Propina, compartir mesa, capacidad, pedido, puntaje del plato y puntaje del mesero

    def __init__(self, customer_id, tip, capacity, order, waiter_score ):
        self._customer_id = customer_id
        self._tip = tip
        self._capacity = capacity
        self._order = order
        self._waiter_score = waiter_score


    def _get_customer_id(self):
        return self._customer_id

    def _get_tip(self):
        return self._tip

    def _get_capacity(self):
        return self._capacity

    def _get_order(self):
        return self._order

    def _get_waiter_score(self):
        return self._waiter_score


    customerId=property(fget=_get_customer_id)
    tip=property(fget=_get_tip)
    capacity=property(fget=_get_capacity)
    order=property(fget=_get_order)
    waiterScore=property(fget=_get_waiter_score)








        