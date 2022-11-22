import numpy as np

from model.Plate import Plate


class Order:

    # def __init__(self, plates):
    #     self.plates=""
    #     self.plates = plates

    def __init__(self):
        # self._var = ""
        self._plates = self.plates =[]


    def addPlates(self,plates):

        self.plates.append(plates)

    def _get_plates(self):
        return self._plates

    def _set_plates(self, plates):
        self._plates=plates

    plates = property(fset=_set_plates, fget=_get_plates)


re = Order()
platess=Plate("r","2","w","s","d","d")
re.addPlates(platess)

# re= np.concatenate((re, "customers"))

print(re.plates)
