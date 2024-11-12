# Write a program named average_calculator.py that reads user input for two integers.
# Assume the user enters positive numbers for both.
# Compute the sum and average of the two numbers and store the result into a variable.
# Then print the result, formatted like the example run below.

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))


sum_num = num1 + num2
avg_num = (num1 + num2) / 2
print(f"The sum of {num1} and {num2} is {sum_num} and the average is {avg_num} ")