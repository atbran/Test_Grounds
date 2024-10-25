import random

scramble_str = input("What would you like to scramble: ")
param = int(input("How long: "))
iterations = int(input("How many iterations would you like: "))
bool_val = int(input("Debug mode? 1: yes, 0: no "))
while bool_val != 1 and bool_val != 0:
    bool_val = int(input("Debug mode? 1: yes, 0: no "))

# Optimized scramble function using random.choices
def scramble(scramble_str, param):
    return ''.join(random.choices(scramble_str, k=len(scramble_str) * param))

# Efficient checker without global variables
def checker(scramble_str, input_str):
    index = input_str.find(scramble_str)
    if index != -1:
        if bool_val == 1:  # Debug output
            print(f"Found '{scramble_str}' at index {index} in the scrambled string.")
            print(f"Substring + or - 5 : {input_str[max(0, index - 5): index + len(scramble_str) + 5]}")
        return True
    return False

def main():
    bound, fails = 0, 0
    while bound < iterations:
        try:
            scrambled = scramble(scramble_str, param)
            if bool_val == 1:
                print(scrambled)  # Debug print

            # Check the result and update counters
            if checker(scramble_str, scrambled):
                bound += 1
            else:
                fails += 1

        except Exception as e:
            print(f"Error: {e}")

    print(f"Total fails: {fails}")

main()
