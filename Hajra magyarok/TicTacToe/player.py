class Player:
    def __init__(self, name, symbol = None, AI = False):
        self.name = name
        self.symbol = symbol
        self.AI = AI
    
    def __repr__(self):
        return self.name
