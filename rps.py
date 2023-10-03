import sys
import random
from enum import Enum

# Global variable
game_count = 0

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def rps():
    global game_count
    player_wins = 0
    python_wins = 0

    def play_rps():
        global game_count  # Add this line to indicate that 'game_count' is a global variable
        playerchoice = input("\nEnter...\n1 for Rock,\n2 for paper, or\n3 for Scissors:\n\n")
        
        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3")
            # Recursion
            return play_rps()
        
        player = int(playerchoice)
        computer = random.randint(1, 3)
        
        print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
        print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")
        
        # Define the decide_winner function
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "You win! Woop Woop"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "You win! Woop Woop"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You win! Woop Woop"
            elif player == computer:
                return "Tie Game!"
            else:
                python_wins += 1
                return "Python wins!"
        
        game_result = decide_winner(player, computer)
        game_count += 1
        print("\nGame count: " + str(game_count))
        print("\nPlayer wins: " + str(player_wins))
        print("\nPython wins: " + str(python_wins))
        
        print("\nPlay again?")
        while True:
            playagain = input("\nY for Yes or\nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        
        if playagain.lower() == "y1":
            return play_rps()
        else:
            print("Congratulations")
            print("Thank you for playing!\n")
            sys.exit("System says Goodbye")

    play_rps()

# Call the main game function
rps()
