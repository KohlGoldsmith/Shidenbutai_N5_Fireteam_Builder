from xml.etree.ElementTree import tostring

from TroopList import Troop
from TroopList import teamTroopList
from TroopList import fireteamLists
#This is checking that each team can only has as many members as specified by its size, 2, 3, or 5 respectively
duo1Count =0
duo2Count=0
duo3Count=0
harrisCount=0
coreCount=0

#Main method for adding a troop from the Fireteam file
def addTroop(fireteamLists):
    global duo1Count
    global duo2Count
    global duo3Count
    global harrisCount
    global coreCount
    print("Senku")
    print("Bushi-tai")
    print("Sayo")
    fireteamChoice = input("Which fireteam do you wish to add to?: ")

    print("Available troops:")
    print("----------------------------")
    print("Senku")
    print("Jizamurai")
    print("Hatamoto")
    print("Taguraida")
    print("Shizoku")
    print("Yamabushi")
    print("Tanuki")
    print("Rui-shi")
    print("Aida Swanson")


    #This is prompting the user to select a troop based off its numerical value after listing all of its properties as defined in the TroopList
    while True:
            troopType= input("Which troop do you wish to add?: ")
            matchingTroops = [troop for troop in teamTroopList if troop.name == troopType and fireteamChoice == troop.teamName]
            if not matchingTroops:
                #Needs the troop to mach a selection
                print("That troop doesn't belong in that fireteam. Pick again.\n")
                continue

                #Shows all troop profiles for the selected basic name
            print("\nMatching Troops:")
            for index, troop in enumerate(matchingTroops, start=1):
                print(f"{index}. Name: {troop.name}, Points: {troop.points}, Weapon: {troop.weapon}, "
                 f"Team Name: {troop.teamName}, Team Size(s): First Size: {troop.teamSizeOne} Second Size:{troop.teamSizeTwo}, "
                 f"Equipment: {troop.equipment}, Specialist: {troop.specialist}, Core: {troop.core}")
            try:
                #This is to select the specific troop based on the number chosen.
                indexChoice = int(input("Choose the Troop number to add: ")) -1
                if 0<= indexChoice < len(matchingTroops):
                    chosenTroop = matchingTroops[indexChoice]
                    print(f"\nSelected Troop: {chosenTroop.name}, Team: {chosenTroop.teamName}, Points: {troop.points}, Weapon: {troop.weapon}, "
                          f"Equipment: {troop.equipment}, Specialist: {troop.specialist}")
                    available_teams= []
                    if chosenTroop.teamSizeOne == 2:
                        available_teams.extend(["Duo 1", "Duo 2", "Duo 3"])
                    if chosenTroop.teamSizeOne ==3:
                        available_teams.extend(["Harris"])
                    if chosenTroop.teamSizeTwo ==3:
                        available_teams.extend(["Harris"])
                    if chosenTroop.teamSizeTwo ==5:
                        available_teams.extend(["Core"])
                    if chosenTroop.teamSizeThree ==5:
                        available_teams.extend(["Core"])


                    team_order = ["Duo 1", "Duo 2", "Duo 3", "Harris", "Core"]

                    available_teams=[team for team in team_order if team in available_teams]

# If available_teams is still empty, warn the user
                    if not available_teams:
                       print("\n⚠️ No valid fireteams available for this troop!")


                    #Determine the team it's being added to
                    print("\nWhich fireteam would you like to add this troop to?")
                    for i, team in enumerate(available_teams, start=1):
                        print(f"{i}. {team}")


                    team_choice = int(input("Enter the number of the fireteam: ")) -1
                    if 0 <= team_choice < len(available_teams)+1:
                        selected_team = available_teams[team_choice]
                        if selected_team in fireteamLists:
                            fireteamLists[selected_team].append(chosenTroop.name)
                            if team_choice == 1 and duo1Count <2:
                                print(f"\nAdded {chosenTroop.name} added to {selected_team} fireteam.")
                                duo1Count+=1
                            if team_choice == 2 and duo2Count <2:
                                print(f"\nAdded {chosenTroop.name} added to {selected_team} fireteam.")
                                duo2Count+=1
                            if team_choice == 3 and duo3Count <2:
                                print(f"\nAdded {chosenTroop.name} added to {selected_team} fireteam.")
                                duo3Count+=1
                            if team_choice == 4 and harrisCount <3:
                                print(f"\nAdded {chosenTroop.name} added to {selected_team} fireteam.")
                                harrisCount+=1
                            if team_choice == 5 and coreCount <5:
                                print(f"\nAdded {chosenTroop.name} added to {selected_team} fireteam.")
                                coreCount+=1
                        else:
                            print("\nError: Selected team doesn't exist or is full.")

                    else:
                        print("\nInvalid Selection. Try again.\n")
                    break
                else:
                    print("Invalid selection. Try again.\n")
            except ValueError:
                print("Please enter a valid number.\n")

