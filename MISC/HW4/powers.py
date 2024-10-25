#does power of a number without using **
#inputs for the number and the power
input_num_1 = int(input("Enter a number: "))
input_num_2 = int(input("Enter its power: "))
#init vars
counter = 1
final_num = 1

#this does the actual powers
while counter <= input_num_2 != 0:
    final_num *= input_num_1
    counter += 1

#set in case of 0
if input_num_2 == 0:
    final_num = 1
print(final_num)