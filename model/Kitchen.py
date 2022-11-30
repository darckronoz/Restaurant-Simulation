
#this class manage the chefs
#gives each chef a plate to make and owns the freezer queue
class Kitchen:
    #chefs: array of 3 different chefs
    #freezer: queue, freezer can only be used by one chef at the time
    def __init__(self, chefs, freezer):
        self.chefs = chefs
        self.freezer = freezer
