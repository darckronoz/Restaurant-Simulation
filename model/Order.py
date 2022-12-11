class Order:

    def __init__(self, id_order, plates):
        # self._var = ""
        self._plates = plates
        self._id_order = id_order

    def _get_id_order(self):
        return self._id_order

    def _get_plates(self):
        return self._plates

    def get_total_order(self):
        total_order = 0
        for i in range(len(self._plates)):
            total_order += self._plates[i].price
        return total_order

    def get_total_time(self):
        total_time = 0
        for i in range(len(self._plates)):
            total_time += self._plates[i].timeService
        return total_time

    plates = property(fget=_get_plates)
    idOrder = property(fget=_get_id_order)
    # totalOrder= property(fget=_get_total_order)
