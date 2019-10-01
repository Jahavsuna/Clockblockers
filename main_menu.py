"""
Created:    Oct 1, 2019
By:         Yahav Lavie
Purpose:    Main menu for Clockblockers game
"""

# IMPORTS
from os import system         #Used to reprint a screen.
import menu_prompts

# CONSTANTS
CLEAR = "clear"
VERSION = 0.1

def main():
    """Game main menu."""
    user_input = -1
    while(user_input != "q"):
        if(user_input == -1):
            c_print(menu_prompts.WELCOME.format(VERSION))
            user_input = raw_input("Choice: ")
        elif(user_input == 1)
    ##test
    c_print(menu_prompts.WELCOME.format(VERSION))

def c_print(string):
    """A wrapper for print that clears the previous screen and displays the menu.
    Receives: string, a string to print.
    Returns: void.
    """
    system(CLEAR)
    print(string)



if __name__ == "__main__":
    main()