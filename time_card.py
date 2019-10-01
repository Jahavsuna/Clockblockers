class Time_card:
    def __init__(self):
        self.top_row = "\/"
        self.bot_row = "/\\"

class card_next_two(Time_card):
    def __init__(self):
        self.top_row = "2 "
        self.bot_row = "->"

class card_prev_two(Time_card):
    def __init__(self):
        self.top_row = "2 "
        self.bot_row = "<-"

class card_next_one(Time_card):
    def __init__(self):
        self.top_row = "1 "
        self.bot_row = "->"

class card_prev_one(Time_card):
    def __init__(self):
        self.top_row = "1 "
        self.bot_row = "<-"

class card_hold(Time_card):
    def __init__(self):
        self.top_row = "HO"
        self.bot_row = "LD"

class card_swap(Time_card):
    def __init__(self):
        self.top_row = "->"
        self.bot_row = "<-"