#this takes a number and prints the power of 2 to that number starting from 1 until that number

input_int = int(input("Enter a number: "))
#this can more easily done with a for loop, however, the assignment requires a while loop.
iterator = 1
while iterator <= input_int:
    print(f"2 to the power {iterator} is {2**iterator}")
    iterator += 1