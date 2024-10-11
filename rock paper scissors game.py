import random

options = ("rock", "paper", "scissor")
player = None

running = True
while running:
    Computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissor): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {Computer}")

    if player == Computer:
        print("It's a tie!")
    elif player == "rock" and Computer == "scissor":
        print("You win!")
    elif player == "scissor" and Computer == "paper":
        print("You win!")
    elif player == "scissor" and Computer == "rock":
        print("You lose!")
    else:
        print("You lose!")

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again != "y":
        running = False

print("Thanks for playing!")
