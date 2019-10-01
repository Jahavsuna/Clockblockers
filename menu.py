"""
Purpose: A class for main menu.
"""
import menu_prompts

class Menu:
    # Private consts
    _version = 0.1

    def __init__(self):
        self.option_list = {"1": _game_start, "q": _quit_game}
        self.welcome = menu_prompts.WELCOME.format(_version, menu_prompts.LOCAL_MULTIPLAYER, menu_prompts.QUIT)
    
    def _game_start():
        pass
    
    def _quit_game():
        exit