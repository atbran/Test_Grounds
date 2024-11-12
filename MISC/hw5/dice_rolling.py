#This program takes input for number of dice to roll and number of sides on the dice
import random

dice_count = int(input("Enter the number of dice to roll (<0 value exits the program): "))
#exits the program if the user enters 0 or a negative number for dicecount
#not the most elegant solution but it matches the question example
if dice_count < 1:
    exit()

dice_sides = int(input("Enter the number of sides on the dice (<0 value exits the program): "))

while dice_count > 1 and dice_sides > 1:
    def dice_rolling(dice, sides):
        total = 0
        print(f"Rolling {dice} dice with {sides} sides")
        for i in range(dice):
            dice_val = random.randint(1, sides)
            print(f"Roll {i + 1}: {dice_val}")
            total += dice_val
        print(f"Total: {total}")

    dice_rolling(dice_count, dice_sides)
    dice_count = int(input("Enter the number of dice to roll: "))
    if dice_count < 1:
        exit()
    dice_sides = int(input("Enter the number of sides on the dice: "))
