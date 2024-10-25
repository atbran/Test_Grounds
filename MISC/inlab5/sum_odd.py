#takes a number from the user and calculates the sum of all odd numbers up to that number
user_input = int(input("Enter a number: "))
#initialize the sum of odd numbers
sum_of_odd = 0

for i in range(1, user_input + 1):
    #if there is no remainder when divided by 2, it is an odd number
    if i % 2 != 0:
        sum_of_odd += i

print(f"Sum of odd numbers to {user_input}: ", sum_of_odd)

