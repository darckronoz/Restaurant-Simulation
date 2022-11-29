
from Order import Order


class Customer:

    #El cliente cuenta con un Id, Propina, compartir mesa, capacidad, pedido, puntaje del plato y puntaje del mesero

    def __init__(self, customer_id, tip, capacity, share):
        self._customer_id = customer_id
        self._tip = tip
        self._capacity = capacity
        self._order=None
        self._waiter_score = None
        self._share_table = share


    def _get_customer_id(self):
        return self._customer_id

    def _get_tip(self):
        return self._tip

    def _get_capacity(self):
        return self._capacity

    def _add_waiter_score(self, waiter_score):
         self._waiter_score=waiter_score

    def _get_waiter_score(self):
        return self._waiter_score


# Metodo para añadir orden a un cliente, no se coloca en los parametros del constructor,
# porque no se crea al crear un cliente, sino solo hasta que se sienta a la mesa, despues de eso si se pasa,
# por medio de este metodo
    def _add_order(self, order):
        self._order=order

    def _get_order(self):
        return self._order


#Se maneja bajo build properties, para llamar los getters y setters
    customer_id=property(fget=_get_customer_id)
    tip=property(fget=_get_tip)
    capacity=property(fget=_get_capacity)
    waiterScore=property(fget=_get_waiter_score, fset=_add_waiter_score)
    order= property(fget=_get_order, fset=_add_order)

# cu=Customer(1,2,3,1)
# ore=Order(1,2)
# cu.order=ore
# print(cu.order.plates)






        