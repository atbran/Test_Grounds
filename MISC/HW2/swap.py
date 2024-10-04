x = input("Enter a number for x: ")
y = input("Enter a number for y: ")
print(f"Before the swap: X = {x}, Y = {y}")

#Uses array (list in python) to swap two inputs.
swap_array = [x,y]
#do the actual swapping
x = swap_array[1]
y = swap_array[0]
# used to test logic
# print(swap_array)
print(f"After the swap: X = {x}, Y = {y}")
