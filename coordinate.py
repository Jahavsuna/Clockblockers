class coordinate:
    DIMENSIONS = 2
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __mul__(self, multiplier):
        self.x = self.x * multiplier
        self.y = self.y * multiplier