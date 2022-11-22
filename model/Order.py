class Order:

    def __init__(self, plates):
        # self._var = ""
        self._plates = plates

    def _get_plates(self):
        return self._plates

    plates = property(fget=_get_plates)


