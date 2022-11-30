
class Chef:

    #chef_id: unique identifier for each chef
    #plates: array of the plates *TO DO*
    #skill: * TO DO * supose to be unique skill for each chef.
    #margin_error: margin of getting a plate with errors.
    #state: True if Ocuped, False if Free.
    #freezer_time: deleted, this time'll be given by the plate recipe.

    def __init__(self, chef_id, plates, skill, margin_error, state):
        self.state = state
        self.margin_error = margin_error
        self.skill = skill
        self.plates = plates
        self.chef_id = chef_id


