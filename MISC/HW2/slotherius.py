import random
print("Slotherius uses the Triple CLAW SLASH!!!!")
sec = int(input("How many seconds would you like to charge: "))

print(f"Attack one: {random.randint(15, 21)}")
print(f"Attack two: {random.randint(15, 21)}")
min_3_attack = 23 - 10 * sec
max_3_attack = 23 + 10 * sec
third_attack = random.randint(min_3_attack, max_3_attack)
print(f"Attack Three: {third_attack}")
