# Every menu has the follow properties:
# Title -- tells what the menu context is 
# Menu selections which have 1) Selection value and 2) Label
# Action associated with the selection (E.g, what happens or what method 
#  needs to be run for each selection)
# *** Data requirements - what needs to be provided for each action to run

from typing import NamedTuple

class MenuStruct(NamedTuple):
    title: str
    selections: dict #key is the selection value, the dict value is label
    actions: dict  #key is the selection value, the dict value is the method that should be called

# define an empty dictionary; applications will need to update it
menus = {}

def AddMenu(menuid, menu_struct):
  menus[menuid] = menu_struct


def ShowMenu(menuid):
    sel_menu = menus[menuid]
    
    # print out the title
    print(sel_menu.title + "\n")
    
    # print out the options  
    for option in sel_menu.selections:
        print(f"\t {option}. {sel_menu.selections[option]}\n")
    
    valid_sel = False;

    while valid_sel != True:
        prompt = "Please enter your selection:"
        # prompt the user for a selection
        user_sel = input(prompt)

        print(f"\nYou selected option {user_sel}")

        # verify whethe the option chosen is appropriate
        # let's check to see if that option is in the list of keys
        action = ""

        try:
            action = sel_menu.actions[user_sel]
            valid_sel = True
        except:
            valid_sel = False
            print("Your selection was invalid. Please try again.")
        
    
    # perform the selected action
    action()