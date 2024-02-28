import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

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
        print(f'Welcome, {name}!')
        playerchoice = input("Enter... \n 1 for Rock\n 2 for Paper\n 3 for Scissors:")

        player = int(playerchoice)

        if playerchoice not in ["1", "2", "3"]:
            print("please enter valid value")
            return play_rps()

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(" ")
        print(f"You chose {str(RPS(player)).replace('RPS.', '')}")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3: 
                player_wins +=1
                return f"{name} wins!"
            elif player == 2 and computer == 1:
                player_wins +=1 
                return f"{name} wins!"
            elif player == 3 and computer == 2:
                player_wins +=1 
                return f"{name} wins!"
            elif player == computer:
                return f"{name} wins!"
            else:
                python_wins +=1
                return "Python Wins"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1
        
        print(f"\n game count: {str(game_count)}")
        print(f"\n {name} Wins: {str(player_wins)}")
        print(f"\n Computer Wins: {str(python_wins)}")
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
    return play_rps



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal game experience"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )

    
    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()