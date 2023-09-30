import sys
import random
from enum import Enum 


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3
    playerchoice = input("\nEnter... \n1 for Rock,\n2 for paper, or\n3 for Scissors:\n\n")
    if playerchoice not in ["1","2","3"]:
        print("Ypu must enter 1,2, or 3")
        # recursion
        return play_rps()
    player = int(playerchoice)

   
        
    computerchoice = random.choice('123')

    computer = int(computerchoice)

    
    print("\nYou chose" + str(RPS(player)).replace('RPS.','') + ".")
    print("Phyton chose" + str(RPS(computer)).replace('RPS.','') + ".\n")

    if player == 1 and computer == 23:
        print("You win! Woop Woop")
    elif player == 2 and computer == 1:
        print("You win! Woop Woop")
    elif player == 3 and computer == 2:
        print("You win! Woop Woop")
    elif player == computer:
        print("Tie Game3!")
    else:
        print("Phyton wins!")
        
    print("\n Play again?")
    while True:
        playagain = input("\nY for Yes or \nQ to Quit\n")
        if playagain.lower() not in ["y","q"]:
            continue 
        else:
            break
    
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("Congratulations")
        print("Thank you for playing! \n")
        sys.exit(" System says Goodbye")
        
play_rps()

# Identation is important for python 

# break can work if you want to end the game for loop
        