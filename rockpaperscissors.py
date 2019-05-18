import os
import random as r

options = {1:"Rock",2:"Paper",3:"Scissors"}

choice = 0
random_choice = 0
play_again = ""

while choice != 4:
    choice = int(input("Enter a choice [1 - Rock, 2 - Paper, 3 - Scissors, 4 - quit]: "))
    if choice == 4:
        print("Program will now terminate.")
        break
    if choice in [1,2,3]:
        random_choice = r.randint(1,3)
        if(choice == random_choice):
            print(f"Player chose {options[choice]} and Opponent chose {options[random_choice]}")
            print("Draw")
            input("Game will now restart\nPress any key to continue...")
            os.system("cls")
        elif( (choice == 1 and random_choice == 2) or (choice == 2 and random_choice == 3) or (choice == 3 and random_choice == 1)):
            print(f"Player chose {options[choice]} and Opponent chose {options[random_choice]}")
            print("Player lose")
            input("Game will now restart\nPress any key to continue...")
            os.system("cls")
        else:
            print(f"Player chose {options[choice]} and Opponent chose {options[random_choice]}")
            print("Player wins")
            input("Game will now restart\nPress any key to continue...")
            os.system("cls")
    else:
        pass
    

# choice = int(input("Enter a choice [1 - Rock, 2 - Paper, 3 - Scissors, 4 - quit]: "))
# random_choice = r.randint(1,3)
# if(choice == random_choice):
#     print(f"Player chose {options[choice]} and Opponent chose {options[random_choice]}")
#     print("Draw")
# elif( (choice == 1 and random_choice == 2) or (choice == 2 and random_choice == 3) or (choice == 3 and random_choice == 1)):
#     print(f"Player chose {options[choice]} and Opponent chose {options[random_choice]}")
#     print("Player lose")
# else:
#     print(f"Player chose {options[choice]} and Opponent chose {options[random_choice]}")
#     print("Player wins")