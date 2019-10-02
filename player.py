import action
import coordinate
from os import system

_DEFAULT_CODE_LENGTH = 5
_CODE_PREPARE_MESSAGE = "{}, please build your code. Z to undo."
_CODE_PREPARE_CURRENT_CODE = "Your code so far:"
_CODE_PREPARE_INPUT_REQUEST = "Code action for section {}:"
_INPUT_CODE_WRONG_VALUE = "Input code should be the index of the desired action."
_MOVE_DIRECTION_PROMPT = "Choose move direction: (E)ast, (W)est, (N)orth, (S)outh."
_PUSH_USER_SELECTION = "Choose another player/barricade to push."
_COORDINATE_INPUT_FORMAT = "x,y:"
_ILLEGAL_TARGET = "Target should be a player or barricade. Try again."
_BARRICADE_USER_SELECTION = "Choose a barricade to remove it, or an unbarricaded tile to barricade it."
_BARRICADE_LIMIT = "A maximum of 10 concurrent barricades are allowed."

class Player:
    def __init__(self, name, symbol, pbm):
        self.name = name
        self.symbol = symbol
        self.code = []
        self._ready_inventory
        self._mediator = pbm
    
    def _ready_inventory(self):
        self.inventory = []
        self.inventory.append(action.action_barricade)
        self.inventory.append(action.action_barricade)
        self.inventory.append(action.action_move)
        self.inventory.append(action.action_move)
        self.inventory.append(action.action_double_move)
        self.inventory.append(action.action_double_move)
        self.inventory.append(action.action_machine_move)
        self.inventory.append(action.action_machine_move)
        self.inventory.append(action.action_push)
        self.inventory.append(action.action_push)
        self._inventory_set = set(self.inventory)
    
    def _get_str_available_actions(self):
        ret_str = ""
        for i in range(self._inventory_set):
            ret_str += "({}) - {}, x{}\n".format(i + 1,\
                                               self._inventory_set[i].get_type(),\
                                               self.inventory.count(self._inventory_set[i]))
        return ret_str

    def _is_input_code_selection_legal(self, user_input):
        if(user_input == "Z" or user_input == "z"):
            return True
        if(not user_input.isdigit()):
            print(_INPUT_CODE_WRONG_VALUE)
            return False
        if(int(user_input < 1 or int(user_input) > len(self._inventory_set))):
            print(_INPUT_CODE_WRONG_VALUE)
            return False
        return True
    
    def _is_input_coord_valid(self, user_coord):
        target = user_coord.split(",")
        if((len(target) != coordinate.coordinate.DIMENSIONS)
        or (not target[0].isdigit() or not target[1].isdigit())):
            return False
        if((int(target[0]) < 1 or int(target[0] > self._mediator.board.size))
        or (int(target[1]) < 1 or int(target[1] > self._mediator.board.size))):
            return False
        return True

    def _choose_selection_handler(self, selection):
        action_type = type(self._inventory_set[code_selection - 1])
        if(action_type is action.action_move
        or action_type is action.action_double_move
        or action_type is action.action_machine_move):
            return self._move_handler()
        elif(action_type is action.action_push):
            return self._push_handler()
        elif(action_type is action.action_barricade):
            return self._barricade_handler()
        else:
            raise()
    
    def _barricade_handler(self):
        print(_BARRICADE_USER_SELECTION)
        print(_BARRICADE_LIMIT)
        print(self._mediator.board)
        target = ""
        while(True):
            target = input(_COORDINATE_INPUT_FORMAT)
            if(self._is_input_coord_valid(target)):
                print("Illegal input. Try again.")
                continue
            target = target.split(",")
            target = coordinate.coordinate(int(target[0], int(target[1])))
            returned_action = action.action_barricade()
            returned_action.designate_target(target)
            return returned_action
    
    def _push_handler(self):
        print(_PUSH_USER_SELECTION)
        print(self._mediator.board)
        target = ""
        while(True):
            target = input(_COORDINATE_INPUT_FORMAT)
            if(self._is_input_coord_valid(target)):
                print("Illegal input. Try again.")
                continue
            target = target.split(",")
            target = coordinate.coordinate(int(target[0], int(target[1])))
            if(not (self._mediator.is_barricaded(target) 
            or self._mediator.is_other_player(target, self.symbol))):
                print (_ILLEGAL_TARGET)
                target = ""
                continue
            returned_action = action.action_push()
            returned_action.designate_target(target)
            return returned_action
    
    def _move_handler(self, move_type):
        move_direction = ""
        while(True):
            print(_MOVE_DIRECTION_PROMPT)
            move_direction = input("Direction: ")
            if(move_direction in ["W", "w"]):
                if(move_type == action.MOVE_TYPES[NORMAL]):
                    return action.action_west()
                elif(move_type == action.MOVE_TYPES[DOUBLE]):
                    return action.action_double_west()
                elif(move_type == action.MOVE_TYPES[MACHINE]):
                    return action.action_machine_west()
            if(move_direction in ["E", "e"]):
                if(move_type == action.MOVE_TYPES[NORMAL]):
                    return action.action_east()
                elif(move_type == action.MOVE_TYPES[DOUBLE]):
                    return action.action_double_east()
                elif(move_type == action.MOVE_TYPES[MACHINE]):
                    return action.action_machine_east()
            if(move_direction in ["N", "n"]):
                if(move_type == action.MOVE_TYPES[NORMAL]):
                    return action.action_north()
                elif(move_type == action.MOVE_TYPES[DOUBLE]):
                    return action.action_double_north()
                elif(move_type == action.MOVE_TYPES[MACHINE]):
                    return action.action_machine_north()
            if(move_direction in ["S", "s"]):
                if(move_type == action.MOVE_TYPES[NORMAL]):
                    return action.action_south()
                elif(move_type == action.MOVE_TYPES[DOUBLE]):
                    return action.action_double_south()
                elif(move_type == action.MOVE_TYPES[MACHINE]):
                    return action.action_machine_south()
    
    def prepare_code(self, code_length = _DEFAULT_CODE_LENGTH):
        prepared_actions_count = 0
        while(prepared_actions_count < 5):
            system("clear")
            print(_CODE_PREPARE_MESSAGE.format(self.name))
            print(self._get_str_available_actions())
            print(_CODE_PREPARE_CURRENT_CODE)
            input_processed = False
            while(not input_processed):
                code_selection = input(_CODE_PREPARE_INPUT_REQUEST.format(prepared_actions_count + 1))
                if(not self._is_input_code_selection_legal(code_selection)):
                    continue #input was illegal - return to start.
                if(code_selection == "Z" or code_selection == "z"):
                    if(prepared_actions_count > 0):
                        self.code[prepared_actions_count] = None
                        prepared_actions_count -= 1
                    continue
                appended_action = self._choose_selection_handler(code_selection)
                code[prepared_actions_count] = appended_action.copy()
                prepared_actions_count += 1
        print("All done!")