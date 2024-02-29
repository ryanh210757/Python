import random
import sys

def guess_number():
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def play_guess_number():
        nonlocal player_wins
        playerchoice = input("\nUser, which number am I thinking of... 1, 2, or 3.\n")
  
        if playerchoice not in ["1", "2", "3"]:
            print("User, please choose 1, 2 or 3")
            return play_guess_number()

        computerchoice = random.choice("123")

        player = int(playerchoice)
        computer = int(computerchoice)

        if playerchoice == computer:
            print("You got it correct!")
            player_wins +=1
        else:
            print("You lost")
        
        game_count += 1
        print(f"\nYou have chosen {playerchoice} I have chosen {computer}")
        print(f"\nPlayer Wins {player_wins}\n Game Count: {game_count}")
        print(f"\nYour winning percent: {player_wins / game_count:.2%}")

