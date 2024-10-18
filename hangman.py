import random

# List of words to choose from
words = ("apple", "orange", "banana", "coconut")

# Hangman ASCII art for each stage of wrong guesses
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

# Function to display the hangman based on wrong guesses
def display_man(wrong_guesses):
    art = hangman_art[wrong_guesses]
    for line in art:
        print(line)

# Function to display the current hint (guessed letters and underscores)
def display_hint(hint):
    print("Current word: ", " ".join(hint))

# Function to display the final answer
def display_answer(answer):
    print(f"The correct word was: {answer}")

# Main function for the game
def main():
    answer = random.choice(words)  # Choose a random word
    hint = ["_"] * len(answer)  # Create a list of underscores to represent the word
    wrong_guesses = 0  # Keep track of wrong guesses
    guessed_letters = set()  # Keep track of guessed letters
    
    print("Welcome to Hangman!")

    while wrong_guesses < 6 and "_" in hint:
        display_man(wrong_guesses)
        display_hint(hint)
        
        guess = input("Guess a letter: ").lower()

        # Ensure valid input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {6 - wrong_guesses} attempts left.")

    # Check if the player won or lost
    if "_" not in hint:
        print("Congratulations! You guessed the word!")
    else:
        display_man(wrong_guesses)
        print("Game over!")

    display_answer(answer)

# Entry point of the program
if __name__ == "__main__":
    main()
