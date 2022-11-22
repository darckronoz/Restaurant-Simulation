
class Plate:

    def __init__(self, plateType, preparationTime, price, quality, score, eating_time):
        self.eating_time = eating_time
        self.score = score
        self.quality = quality
        self.price = price
        self.preparationTime = preparationTime
        self.plateType = plateType

    def _get_plates(self):
        return self._plates

    def _set_plates(self, plates):
        self._plates=plates

    plates = property(fset=_set_plates, fget=_get_plates)

        
