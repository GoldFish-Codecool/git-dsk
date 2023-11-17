class Area
    def __init__(self, area_id):
        self.area_id = area_id
        self.intro = ""
        self.choices = []
        self.outros = []
        self.attribute_updates = []
        self.next_area = ""

    class Area1
        intro = "Welcome to Area 1 - enter all description text"
        choices = ["Choice 1", "Choice 2", "Choice 3"]
        outros = ["Outro 1", "Outro 2 - enter outro text corresponding to Choice 2", "Outro 3"]
        attribute_updates = [[health: -1, alcohol: 1, chairman: 0]; [health: 0, alcohol: 0, chairman: -1]; [health: 0, alcohol: 0, chairman: -1]]
        next_area = Area2
        
    class Area2
        intro = "Welcome to Area 1 - enter all description text"
        choices = ["Choice 1", "Choice 2", "Choice 3"]
        outros = ["Outro 1", "Outro 2 - enter outro text corresponding to Choice 2", "Outro 3"]
        attribute_updates = [[health: -1, alcohol: 1, chairman: 0]; [health: 0, alcohol: 0, chairman: -1]; [health: 0, alcohol: 0, chairman: -1]]
        next_area = Area3
        
    class Area3
        intro = "Welcome to Area 1 - enter all description text"
        choices = ["Choice 1", "Choice 2", "Choice 3"]
        outros = ["Outro 1", "Outro 2 - enter outro text corresponding to Choice 2", "Outro 3"]
        attribute_updates = [[health: -1, alcohol: 1, chairman: 0]; [health: 0, alcohol: 0, chairman: -1]; [health: 0, alcohol: 0, chairman: -1]]
        next_area = Area4
