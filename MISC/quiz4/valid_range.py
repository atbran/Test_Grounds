lower_limit = 10
upper_limit = 40

num = int(input("Please enter your number: "))

while lower_limit > num or num > upper_limit:
    print("Sorry, the number must be between 10 and 40. Please try again.")
    num = int(input("Please enter your number: "))

print(f"Your number is {num}. This is a valid number.")