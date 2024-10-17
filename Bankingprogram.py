def show_balance():
    print(f"The balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to be deposited: "))
    if amount < 0:
        print("That's not a valid amount.")
        return 0
    else:
        return amount

def withdrawal():
    global balance  # We need to modify the balance in this function
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
        return 0
    elif amount < 0:
        print("That's not a valid amount.")
        return 0
    else:
        balance -= amount
        print(f"Withdrawal successful! You withdrew ${amount:.2f}")
        return amount

# Initialize variables
balance = 0
is_running = True

# Main loop
while is_running:
    print("\nBanking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        withdrawal()
    elif choice == '4':
        is_running = False
    else:
        print("The choice entered is invalid.")

print("Thank you, have a nice day!")
