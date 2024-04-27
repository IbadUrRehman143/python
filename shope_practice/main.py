from add_item import * 
from tile import *

def menu():
    print("1. Add item ")
    print("2. Show item ")
    print("0. Quit ")

choice = 1
while choice != 0 :
    menu()
    choice = input("Select One Option(1, 2): ")
    choice = int(choice) 
    if choice == 1:
        item_input()

    if choice == 2:
        pass