#this program calculates the factorial of a number without using math package or recursion
input_num_1 = int(input("Enter a number: "))
#init vars
counter = 1
final_num = 1

#does the factorial
while counter <= input_num_1 != 0:
    final_num *= input_num_1 - counter + 1
    counter += 1

#works for 0
if input_num_1 == 0:
    final_num = 1
print(final_num)