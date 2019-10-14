# IMPORTS
import player
import board
import time_card
import player_board_mediator
from os import system

# CONSTANTS
_ADD_PLAYER_STRING = "Player {} name: "
_ADD_PLAYER_SYMBOL = "Player {} symbol: "
_SYMBOL_USED_BY_PLAYER = "Symbol in use by another player! Please choose a different one."
_SYMBOL_USED_BY_SYSTEM = "Symbol is in use by the game! Please choose a different one."
_SYMBOL_LENGTH_ERROR = "Symbols must be single-characters."
_PLAYER_IMPORPER_NAME = "Player name should be 1 to 20 characters."
_PLAYER_SELECT_TIME_CARD = "{}, please select a time card."
_INVALID_TIME_CARD_INDEX = "Invalid index. Time card indexes are written below the cards."
_SWAP_CARD_SELECT_PLAYER = "Select the symbool of the player with whom you wish to swap cards."
_BOARD_SIDE_LENGTH = 9

_RESERVED_SYMBOLS: ['[', ']', 'X', 'x', '|', '-', '^', '$', '@']

class Game_manager:
    def __init__(self, num_of_players, display_module, board_size = _BOARD_SIDE_LENGTH):
        self.player_list = []
        self.board = board.Board(board_size)
        for i in range(num_of_players):
            self.symbol_to_player = {}
            self.player_list.append(self._add_player(i))
            self._update_player_location(self.player_list[i], (board.Board.relative_start_positions[i] * board_size))
        self._create_time_cards()
        self.pointer_index = 0
        self.display_module = display_module

    def _add_player(self, player_index):
        p_name = input(_ADD_PLAYER_STRING.format(player_index + 1))
        while(len(p_name > 20)):
            print(_PLAYER_IMPORPER_NAME)
            p_name = input(_ADD_PLAYER_STRING.format(player_index + 1))
        p_symbol = input(_ADD_PLAYER_SYMBOL.format(player_index + 1))
        while(not self._is_player_symbol_ok):
            p_symbol = input(_ADD_PLAYER_SYMBOL.format(player_index))
        new_player = player.Player(p_name, p_symbol, player_board_mediator(self.board))
        self.symbol_to_player[p_symbol] = new_player
        return new_player

    def _is_player_symbol_ok(self, new_symbol):
        if(len(new_symbol) != 1):
            print(_SYMBOL_LENGTH_ERROR)
            return False
        if(new_symbol in _RESERVED_SYMBOLS):
            print(_SYMBOL_USED_BY_SYSTEM)
            return False
        if(new_symbol in [p.symbol for p in self.player_list]):
            print(_SYMBOL_USED_BY_PLAYER)
            return False
        return True
    
    def _create_time_cards(self):
        self.available_cards = []
        self.available_cards.append(time_card.card_hold())
        self.available_cards.append(time_card.card_swap())
        self.available_cards.append(time_card.card_next_one())
        self.available_cards.append(time_card.card_next_two())
        self.available_cards.append(time_card.card_prev_one())
        self.available_cards.append(time_card.card_prev_two())
    
    def _update_player_location(self, player_symbol, new_location):
        self.board.remove_at_index(self.symbol_to_player[player_symbol].location)
        self.symbol_to_player[player_symbol].set_location(new_location)
        self.board.place_at_index(new_location, player_symbol)
    
    def _get_str_available_time_cards(self):
        print_str = ""
        print_str += ("  ----  ") * len(self.available_cards) + '\n'
        for card in self.available_cards:
            print_str += "  |" + card.top_row + "|  "
        print_str += '\n'
        for card in self.available_cards:
            print_str += "  |" + card.bot_row + "|  "
        print_str += '\n'
        print_str += ("  ----  ") * len(self.available_cards) + '\n'
        for i in range(len(self.available_cards)):
            print_str += "   {}    ".format(i)
        print_str += '\n'
        return print_str

    def _get_str_players(self):
        print_str = ""
        for p in self.player_list:
            player_display = ("{} ({})".format(p.name, p.symbol))
            print_str += player_display + (25 - len(player_display))*" "
        print_str += '\n'
        for p in self.player_list:          #length per player: (2+2+1)*5 columns
            for c in p.code:
                print_str += "[" + c.top_row + "] "
        print_str += '\n'
        for p in self.player_list:          #length per player: (2+2+1)*5 columns
            for c in p.code:
                print_str += "[" + c.bot_row + "] "
        #Now I need to generate the pointer
        pointer_print_index = self.pointer_index * 5
        pointer_appendix = pointer_print_index * " " + "^" + 4 * (25 * " " + "^")
        print_str += pointer_appendix
        return print_str

    def _show_board(self):
        print("REMAINING TIME CARDS:")
        print(self._get_str_available_time_cards())
        print(self.board)
        print(self._get_str_players())
    
    def _swap_action_handler(self,active_player):
        print(_SWAP_CARD_SELECT_PLAYER)
        print(self._get_str_players)
        valid_target_selected = False
        while(not valid_target_selected):
            try:
                target_player_symbol = input("Player symbol: ")
                target = self.symbol_to_player[target_player_symbol]
                if(target is active_player):
                    raise ValueError
                valid_target_selected = True
            except KeyError:
                print("Please select a valid player symbol.")
            except ValueError:
                print("You cannot swap with yourself. Please try again.")
        print(target.get_code_string())
        valid_taken_action_selected = False
        while(not valid_taken_action_selected):
            try:
                target_action_index = input("Target action you want to take: ")
                taken_action = target.code[target_action_index - 1]
                valid_taken_action_selected = True
            except ValueError:
                print("Invalid action index.")
        valid_given_action_selected = False
        while(not valid_given_action_selected):
            try:
                given_action_index = input("Target action you want to take: ")
                given_action = active_player.code[given_action_index - 1]
                valid_given_action_selected = True
            except ValueError:
                print("Invalid action index.")
        temp_action = taken_action.copy()
        target.code[target_action_index - 1] = given_action.copy()
        active_player.code[given_action_index - 1] = temp_action.copy()

    def run_game(self):
        #TODO: Create a D.I. object for display.
        is_game_won = False
        round_index = 1
        while(not is_game_won):
            # A single game round
            self._show_board()
            for p in self.player_list:
                p.prepare_code()
            while(len(self.available_cards) > 0):
                # Rounds in which we still use the same game code
                active_player = self.player_list[round_index % len(self.player_list)]
                print(_PLAYER_SELECT_TIME_CARD.format(active_player.name))
                selected_time_card_index = input("Time card index: ")
                while(not (selected_time_card_index.isdigit()
                           and int(selected_time_card_index) > 0
                           and int(selected_time_card_index) < len(self.available_cards))):
                    print(_INVALID_TIME_CARD_INDEX)
                    print(self._get_str_available_time_cards)
                selected_time_card = self.available_cards.pop(selected_time_card_index) # Pop already removes from list
                if(type(selected_time_card) is time_card.card_swap):
                    self._swap_action_handler(active_player)
                else:
                    # TODO: Execute the various actions.
                for p in self.player_list:
                    # The chosen card affects each player

if __name__ == "__main__":
    #tests
    #g = Game_manager(1)
    #g.run_game()
    print("end!")