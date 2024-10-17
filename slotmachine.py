import random

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    # Print the row of symbols with spaces between them
    print(" | ".join(row))

def get_payout(row, bet):
    # Payout logic: e.g., match 3 symbols for a big win, 2 for smaller win
    if row[0] == row[1] == row[2]:
        print("Jackpot! All three symbols match!")
        return bet * 10  # Example payout: 10 times the bet for 3 matching symbols
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        print("You matched two symbols!")
        return bet * 2  # Example payout: 2 times the bet for 2 matching symbols
    else:
        print("No match, better luck next time!")
        return 0  # No payout

def main():
    balance = 100
    print("Welcome to Python Slots!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    
    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Place your amount: ")
        
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient funds!")
            continue
        if bet <= 0:
            print("Bet must be greater than 0.")
            continue
        
        balance -= bet
        row = spin_row()
        
        print("Spinning...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        balance += payout
        
    print("Game over! You're out of balance.")

if __name__ == '__main__':
    main()
