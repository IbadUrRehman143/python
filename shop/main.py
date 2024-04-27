from add_item import *
from tile import *

def menu():
    print("1. Add item")
    print("2. Show items")
    print("0. Quit")

choice = 1
while choice != 0:
    menu()
    choice = input("Select one option(1, 2): ")
    choice=int(choice)
    if choice==1:
        item_input()

    if choice==2:
        for i in range(len(items)):
            tile(items[i])