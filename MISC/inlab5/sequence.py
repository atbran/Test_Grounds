
#geometric sequence
# a(n) = a(1) * r^(n-1)

#takes an input from the user
print("This program will calculate the first n numbers of a geometric sequence.")
print("The sequence is defined as a(n) = 3 * 2^(n-1)")
user_input = int(input("Enter a number: "))


print(f"The first {user_input + 1} numbers of the geometric sequence are:")

#does the actual math
for i in range(1, user_input + 1):
    print(3*1*2**(i-1))

