import coordinate

MOVE_TYPES = {"NORMAL" : 1, "DOUBLE" : 2, "MACHINE" : 3}

class Action:
    def __init__(self):
        self.top_row = "\/"
        self.bot_row = "/\\"
    
    def get_type(self):
        return "Uninitialized"
    
    def copy(self):
        return Action()

class action_move(Action):
    def __init__(self):
        pass

    def get_type(self):
        return "Move action"
    
    def copy(self):
        return action_move()

class action_double_move(Action):
    def __init__(self):
        pass
        
    def get_type(self):
        return "Double move action"
    
    def copy(self):
        return action_double_move()

class action_machine_move(Action):
    def __init__(self):
        pass
        
    def get_type(self):
        return "Machine move action"
    
    def copy(self):
        return action_machine_move()

class action_west(Action):
    def __init__(self):
        self.top_row = "@ "
        self.bot_row = "<-"
    
    def copy(self):
        return action_west()

class action_east(Action):
    def __init__(self):
        self.top_row = "@ "
        self.bot_row = "->"
    
    def copy(self):
        return action_east()

class action_north(Action):
    def __init__(self):
        self.top_row = "@^"
        self.bot_row = " |"
    
    def copy(self):
        return action_north()

class action_south(Action):
    def __init__(self):
        self.top_row = "@|"
        self.bot_row = " V"
    
    def copy(self):
        return action_south()

class action_double_west(Action):
    def __init__(self):
        self.top_row = "@2"
        self.bot_row = "<-"
    
    def copy(self):
        return action_double_west()

class action_double_east(Action):
    def __init__(self):
        self.top_row = "@2"
        self.bot_row = "->"
    
    def copy(self):
        return action_double_east()

class action_double_north(Action):
    def __init__(self):
        self.top_row = "@^"
        self.bot_row = "2|"
    
    def copy(self):
        return action_double_north()

class action_double_south(Action):
    def __init__(self):
        self.top_row = "@|"
        self.bot_row = "2V"
    
    def copy(self):
        return action_double_south()

class action_machine_south(Action):
    def __init__(self):
        self.top_row = "$|"
        self.bot_row = " V"
    
    def copy(self):
        return action_machine_south()

class action_machine_north(Action):
    def __init__(self):
        self.top_row = "$^"
        self.bot_row = " |"
    
    def copy(self):
        return action_machine_north()

class action_machine_east(Action):
    def __init__(self):
        self.top_row = "$ "
        self.bot_row = "->"
    
    def copy(self):
        return action_machine_east()

class action_machine_west(Action):
    def __init__(self):
        self.top_row = "$ "
        self.bot_row = "<-"
    
    def copy(self):
        return action_machine_west()

class action_barricade(Action):
    def __init__(self):
        self.top_row = "\/"
        self.bot_row = "/\\"
    
    def designate_target(self, coord):
        self.target = coord
    
    def copy(self):
        copy = action_barricade()
        copy.designate_target(self.target)
        return copy()

class action_push(Action):
    def __init__(self):
        self.top_row = "PU"
        self.bot_row = "SH"
    
    def designate_target(self, coord):
        self.target = coord
    
    def copy(self):
        copy = action_barricade()
        copy.designate_target(self.target)
        return copy()