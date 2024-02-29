import random
import sys

def guess_number(name = 'PlayerOne'):
    game_count = 0
    player_wins = 0

    
    def play_guess_number():
        nonlocal player_wins
        nonlocal name

        playerchoice = input("\nUser, which number am I thinking of... 1, 2, or 3.\n")
  
        if playerchoice not in ["1", "2", "3"]:
            print("User, please choose 1, 2 or 3")
            return play_guess_number()

        computerchoice = random.choice("123")

        player = int(playerchoice)
        computer = int(computerchoice)
        
        def decide_winner(player, computer):
        
            if player == computer:
                player_wins +=1
                return ("You got it correct!")
            else:
                return ("You lost")
            
        game_result = decide_winner(player, computer)
        print(game_result)
        nonlocal game_count    
        game_count += 1
        print(f"\nYou have chosen {playerchoice} I have chosen {computer}")
        print(f"\nPlayer Wins {player_wins}\n Game Count: {game_count}")
        print(f"\nYour winning percent: {player_wins / game_count:.2%}")

        print("Play again?")
        while True:
            playagain = input("\nY for Yes\nQ to Quit")
            if playagain.lower() not in ["y", "q"]:
                print("please print a valid option")
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_guess_number()
        else:
            print("\nBye for now\n")
            if __name__=="__main__":
                sys.exit(f"Bye {name}!")
            else:
                return
    
    play_guess_number()



guess_number()


