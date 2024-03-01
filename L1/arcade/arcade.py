import sys
from rps import rps
from guess_number import guess_number

print(f"\nUser, welcome to the arcade!\n")

print("Please choose a game\n")

def play_game(name='PlayerOne'):
    weclome_back = False

    while True:
        if weclome_back == True:
            print("Welcome back to the aracde")

        selected_game = input(f"\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"X\" to exit the Arcade\n\n")
        if selected_game not in ["1", "2", "x"]:
            print("User, please enter 1, 2 or x")
            return play_game(name)

        weclome_back = True
        
        if selected_game == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            print("See you next time")

if __name__ == "__main__":
    play_game()
        
    