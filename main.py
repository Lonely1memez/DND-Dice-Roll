# Name: Antonio Mora
#Date: 12/2/2021
#Program: DnD Dice Roll / Self Project
#Function: To give out outcome of the dices in a DnD

import random

# Function to roll a specific type of dice a given number of times
def roll_dice(dice_type, num_rolls=1):
    results = []
    for _ in range(num_rolls):
        result = random.randint(1, dice_type)
        results.append(result)
    return results

# Function to roll a specific type of dice a given number of times and calculate the sum
def roll_and_sum(dice_type, num_rolls=1):
    rolls = roll_dice(dice_type, num_rolls)
    total = sum(rolls)
    return total

# Define a list of all the common types of dice
dice_types = [4, 6, 8, 10, 12, 20]

# Specify the number of rolls for each type of dice
num_rolls = 1

# Loop through each type of dice and roll it
for dice_type in dice_types:
    # Roll the dice and calculate the total outcome
    total = roll_and_sum(dice_type, num_rolls)
    
    # Print the results, including the total outcome and individual roll results
    print(f"Rolling {num_rolls}d{dice_type}: {total} ({', '.join(map(str, roll_dice(dice_type, num_rolls)))})")
