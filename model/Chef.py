
class Chef:
    def __init__(self, chef_id, plates, skill, margin_error, state, freezer_time):
        self.freezer_time = freezer_time
        self.state = state
        self.margin_error = margin_error
        self.skill = skill
        self.plates = plates
        self.chef_id = chef_id
