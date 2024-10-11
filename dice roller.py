import random

import random

dice_art = [
    ["┌─────────┐",
     "│         │",
     "│    ●    │",
     "│         │",
     "└─────────┘"],
    ["┌─────────┐",
     "│●        │",
     "│         │",
     "│       ● │",
     "└─────────┘"],
    ["┌─────────┐",
     "│●        │",
     "│    ●    │",
     "│        ●│",
     "└─────────┘"],
    ["┌─────────┐",
     "│●       ●│",
     "│         │",
     "│●       ●│",
     "└─────────┘"],
    ["┌─────────┐",
     "│●       ●│",
     "│    ●    │",
     "│●       ●│",
     "└─────────┘"],
    ["┌─────────┐",
     "│●       ●│",
     "│●       ●│",
     "│●       ●│",
     "└─────────┘"]
]

dice = []
total = 0
num_of_dice = int(input("How many dice do you want to roll? "))

for _ in range(num_of_dice):
    roll = random.randint(1, 6)
    dice.append(roll)

for die in dice:
    total += die

# Display the rolled dice
for die in dice:
    print("\n".join(dice_art[die - 1]))
    print()  # Add a space between dice

print(f"Total: {total}")
