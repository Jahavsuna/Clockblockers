import coordinate

MOVE_TYPES = {"NORMAL" : 1, "DOUBLE" : 2, "MACHINE" : 3}

class Action:
    def __init__(self):
        self.top_row = "\/"
        self.bot_row = "/\\"
    
    def get_type(self):
        return "Uninitialized"

class action_move(Action):
    def __init__(self):
        pass

    def get_type(self):
        return "Move action"

class action_double_move(Action):
    def __init__(self):
        pass
        
    def get_type(self):
        return "Double move action"

class action_machine_move(Action):
    def __init__(self):
        pass
        
    def get_type(self):
        return "Machine move action"

class action_west(Action):
    def __init__(self):
        self.top_row = "@ "
        self.bot_row = "<-"

class action_east(Action):
    def __init__(self):
        self.top_row = "@ "
        self.bot_row = "->"

class action_north(Action):
    def __init__(self):
        self.top_row = "@^"
        self.bot_row = " |"

class action_south(Action):
    def __init__(self):
        self.top_row = "@|"
        self.bot_row = " V"

class action_double_west(Action):
    def __init__(self):
        self.top_row = "@2"
        self.bot_row = "<-"

class action_double_east(Action):
    def __init__(self):
        self.top_row = "@2"
        self.bot_row = "->"

class action_double_north(Action):
    def __init__(self):
        self.top_row = "@^"
        self.bot_row = "2|"

class action_double_south(Action):
    def __init__(self):
        self.top_row = "@|"
        self.bot_row = "2V"

class action_machine_south(Action):
    def __init__(self):
        self.top_row = "$|"
        self.bot_row = " V"

class action_machine_north(Action):
    def __init__(self):
        self.top_row = "$^"
        self.bot_row = " |"

class action_machine_east(Action):
    def __init__(self):
        self.top_row = "$ "
        self.bot_row = "->"

class action_machine_west(Action):
    def __init__(self):
        self.top_row = "$ "
        self.bot_row = "<-"

class action_barricade(Action):
    def __init__(self):
        self.top_row = "\/"
        self.bot_row = "/\\"
    
    def designate_target(self, coord, is_add_action):
        self.target = coord
        self.add_barricade = is_add_action

class action_push(Action):
    def __init__(self):
        self.top_row = "PU"
        self.bot_row = "SH"
    
    def designate_target(self, coord):
        self.target = coord