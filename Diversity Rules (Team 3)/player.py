class Player:
    def __init__(self, name):
        self.name = name
        self.health = 3
        self.alcohol = 0
        self.chairman = 0
        self.location = 1 #starts with 1, as that is the 1st location (Area 1) #we need to update location too
        self.statuses = {
            "jail": 0,
            "fired": 0,
            "injured": 0
        }

    def update_status(self, status, value):
        self.statuses[status] += value

    def get_status(self, status):
        return self.statuses[status]

    def update_health(self, value):
        self.health += value

    def update_alcohol(self, value):
        self.alcohol += value

    def update_chairman(self, value):
        self.chairman += value

    def get_promoted(self):
        if self.chairman > 5:
            return "Promotion"

    def check_health(self):
        if self.health <= 0:
            self.update_status("injured", 1)

    def check_alcohol(self):
        if self.alcohol > 3:
            self.update_status("jail", 1)

    def check_chairman(self):
        if self.chairman <= -5:
            self.update_status("fired", 1)
