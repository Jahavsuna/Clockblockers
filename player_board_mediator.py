import board

class player_board_mediator:
    def __init__(self, board):
        self.board = board
    
    def is_barricaded(self, coord):
        return (board.barricade == self.board.get_item_at_index(coord))
    
    def is_other_player(self, coord, active_symbol):
        item_at_index = self.board.get_item_at_index(coord)
        if(item_at_index == board.barricade):
            return False
        if(item_at_index == board.blank):
            return False
        if(item_at_index == board.time_machine):
            return False
        if(item_at_index == active_symbol):
            return False
        return True