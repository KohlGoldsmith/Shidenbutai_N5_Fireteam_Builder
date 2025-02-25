import TroopList
from AddTroop import addTroop
from TroopList import fireteamLists

from AddTroop import duo1Count
from AddTroop import duo2Count
from AddTroop import duo3Count
from AddTroop import harrisCount
from AddTroop import coreCount
import os
def open_in_new_terminal():
    os.system("osascript -e 'tell application \"Terminal\" to do script \"python3 Fireteam.py\"'")


unitPointCount=[]
current_list_index=0

def print_menu():
    print("\n----------Menu----------")
    print("Team 1 = Duo 1, Team 2 = Duo 2, Team 3 = Duo 3, Team 4 = Harris, Team 5 = Core")
    print("1. View current teams")
    print("2. Add a unit to a team")
    print("3. Remove a unit from the current team")
    print("4. Exit")
    print("----------------------------")

def view_team():
    print("\nCurrent Fireteam Lists\n")

    for team_name, troop_list in fireteamLists.items():
        print(f" {team_name}:")
        if troop_list:
            for troop in troop_list:
                if isinstance(troop, str):  # If stored as a name
                    print(f"   - {troop}")
                else:  # If stored as a Troop object
                    print(f"   - {troop.name} (Points: {troop.points}, Weapon: {troop.weapon})")
        else:
            print("   - (Empty)")
        print("-" * 30)  # Separator for readability


def remove_troop():
    view_team()
    try:
        item = input("Enter the item to remove: ")
        team_lists[current_list_index].remove(item)
        print(f"Removed '{item}' from List {current_list_index + 1}.")
    except ValueError:
        print(f"'{item}' not found in List {current_list_index + 1}.")


# Main program loop
while True:
    print_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        view_team()
    elif choice == "2":
        addTroop(fireteamLists)
    elif choice == "3":
        remove_troop()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

