from rps import func

print(f"\nUser, welcome to the arcade!\n")

print("Please choose a game\n")


while True:
    selected_game = input(f"\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"X\" to exit the Arcade\n\n")
    if selected_game not in ["1", "2", "X"]:
        print("User, please enter 1, 2 or X")
        continue
    else:
        break
    
if selected_game == 2:
    func()
    
    