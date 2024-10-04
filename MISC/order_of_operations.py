
#The first step of the operation is to do 10-6. This equals 4
operation_1_part_1 = 10-6
#the next step is calculate 15 //4 which means that is 'floored' to the lower value. This equals 3
operation_1_part_2 = 15 //4
#next step is to multiply together steps 1 and 2. This should equal 12.
operation_1_final = operation_1_part_1 * operation_1_part_2
print(f"Here is the step by step set of operations to solve problem 1: {operation_1_final}")
print(f"It should be the same as this value here: {15 // 4 * (10 - 6)} \n")

#for operation two, the first step is to solve this expression: (30 // 6 + 4). This should equal 9

operation_2_part_1 = (30 // 6 + 4)
#the next step is to do the other set of parenthesis. This should also equal 9.
operation_2_part_2 = (18 - 9)
#next step is to multiply the two these two parts of the expression. (30 // 6 + 4) * (18 - 9) They are stored as:
#(30 // 6 + 4) as operation_2_part_1 and (18 - 9) as operation_2_part_2. This should equal 81.
operation_2_part_3 = operation_2_part_1 * operation_2_part_2
#final step is to divide part 3 by 3; we should also keep in mind that the value should also be floored. This should equal 27.
operation_2_final = operation_2_part_3 // 3

print(f"Here is the step by step set of operations to solve problem 2: {operation_2_final}")
print(f"It should be the same as this value here: {(30 // 6 + 4) * (18 - 9) // 3}")