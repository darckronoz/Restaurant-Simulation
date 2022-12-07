from model.PlateTypeEnum import PlateTypeEnum


class Plate:

    def __init__(self,id_plate, plate_name, preparationTime, price, score, eating_time, plate_type):
        self._id_plate=id_plate
        self._plate_name=plate_name
        self._eating_time = eating_time
        self._score = score
        self._price = price
        self._preparation_time = preparationTime
        self._plate_type=PlateTypeEnum(plate_type)

    def _get_eating_time(self):
        return self._eating_time

    def _get_name(self):
        return self._plate_name

    def _get_score(self):
        return self._score

    def _get_price(self):
        return self._price

    def _get_preparation_time(self):
        return self._preparation_time

    def _get_plate_type(self):
        return self._plate_type

    def _get_total_time_service(self):
        return self.eatingTime+self.preparationTime

    def _get_id_plate(self):
        return self._id_plate

    eatingTime=property(fget=_get_eating_time)
    name=property(fget=_get_name)
    score=property(fget=_get_score)
    price=property(fget=_get_price)
    preparationTime=property(fget=_get_preparation_time)
    plateType=property(fget=_get_plate_type)
    timeService=property(fget=_get_total_time_service)
    idPlate=property(fget=_get_id_plate)
