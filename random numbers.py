import random
from xml.sax.handler import property_interning_dict

lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)
guesses=0
is_running=True

print("Python Number Guessing game")
print(f"Select a number between{lowest_num}  and {highest_num}")

while is_running:

    guess=(input("Guess a number: "))

    if guess.isdigit():
        guess=int(guess)
        guesses+=1

        if guess< lowest_num or guess> highest_num:
            print("Guess is out of range")
            print(f"Try again a number that is between {lowest_num} and {highest_num}")
        elif guess< answer:
            print("Guess is too low")
        elif guess> answer:
            print("Guess is too high")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"You guessed it in {guesses} guesses")
            is_running=False
    else:
        print("invalid guess")
        print("Try again")