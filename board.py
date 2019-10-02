import coordinate

class Board:
    barricade = "X"
    blank = " "
    time_machine = "$"
    relative_start_positions = [coordinate.coordinate(0,0),\
                                coordinate.coordinate(1,1),\
                                coordinate.coordinate(1,0),\
                                coordinate.coordinate(0,1)]

    def __init__(self, size):
        self.cells = []
        self.size = size
        for i in range(size):
            self.cells.append([])
    
    def get_item_at_index(self, coord):
        return self.cells[coord.x][coord.y]
    
    def get_index_of_item(self, symbol):
        for col in cells:
            for row in col:
                if(self.cells[col][row] == symbol):
                    return coordinate.coordinate(col, row)
        raise()
    
    def remove_at_index(self, coord):
        cells[coord.x][coord.y] = Board.blank
    
    def place_at_index(self, coord, symbol):
        cells[coord.x][coord.y] = symbol