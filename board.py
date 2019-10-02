import coordinate

class Board:
    barricade = "X"
    blank = " "
    time_machine = "$"

    def __init__(self, size):
        self.cells = []
        self.size = size
        for i in range(size):
            self.cells.append([])
    
    def get_item_at_index(self, coord):
        return self.cells[coord.x][coord.y]