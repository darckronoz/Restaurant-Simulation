import numpy as np


class Order:

    def __init__(self, id_order, plates):
        # self._var = ""
        self._plates = [plates]
        self._id_order=id_order

    def _get_id_order(self):
        return self._id_order
    
    def _get_plates(self):
        return self._plates

    plates = property(fget=_get_plates)
    idOrder= property(fget=_get_id_order)


