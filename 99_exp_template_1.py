"""
Created on May 18, 2019 at 05:01 PM



"""

# import the goodies
import os, sys, time
import datetime

import pyautogui


def main(): #{
    print("todd")
    ## CONFIRM MACRO ACTION VIA USER INPUT
    choiceStr = pyautogui.confirm(text='select action to ATTEMPT to run:', title='FUCK_MAX_PETTI',
                      buttons=['FISH', "FLETCHING", "MINING", "HERBLAW", "PRAYER", "SMITHING", "WOOD"])
    print("USER CHOICE == " + choiceStr)
    #########################################
    if choiceStr == "FISH": #{
        print("FISHING....\n")
    #}
    elif choiceStr == "FLETCHING": #{
        print("FLETCHING...\n")
    #}
    elif choiceStr == "MINING": #{
        print("MINING...\n")
    #}
    elif choiceStr == "HERBLAW": #{
        print("HERBLAW...\n")
    #}
    elif choiceStr == "PRAYER": #{
        print("PRAYER...\n")
    #}
    elif choiceStr == "SMITHING": #{
        print("SMITHING...\n")
    #}
    elif choiceStr == "WOOD": #{
        print("WOOD...\n")

    #]



#]

if __name__ == "__main__":
    main()