class Box:
    def __init__(self, address, date_posted, weight):
        self.address = address
        self.date_posted = date_posted
        self.weight = weight
        if weight <= 1000:
            self.price = 7.99
        else:
            self.price = 10.29 + 0.29 * (weight - 1000)
