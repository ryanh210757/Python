import sys
import random
from enum import Enum
game_count = 0

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # print(RPS(1))
    # print(RPS['ROCK'])
    # print(RPS.ROCK)
    # print(RPS.ROCK.value)
    # #sys.exit()

    print(" ")

    playerchoice = input("Enter... \n 1 for Rock\n 2 for Paper\n 3 for Scissors:")

    player = int(playerchoice)

    if playerchoice not in ["1", "2", "3"]:
        print("please enter valid value")
        return play_rps()

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print(" ")
    print("You chose" + str(RPS(player)).replace('RPS.', ''))
    print("Python chose" + str(RPS(computer)).replace('RPS.', ''))

    def decide_winner(player, computer):
        if player == 1 and computer == 3: 
            return "You win!"
        elif player == 2 and computer == 1: 
            return "You win!"
        elif player == 3 and computer == 2: 
            return "You win!"
        elif player == computer:
            return "tie game"
        else:
            return "Python Wins"

    game_result = decide_winner(player, computer)
    print(game_result)
    global game_count
    game_count += 1
    print("\n game count:" + str(game_count))
    print("would you like to play again?")
    while True:
        playagain = input("Enter Y or Q")
        if playagain.lower() not in ["y", "q"]:
            print("Wrong value entered")
            continue
        else:
            break
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("Thanks for playing")
        sys.exit("Bye!")

play_rps()