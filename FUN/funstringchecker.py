from random import randint

scramble_str = str(input("What would you like to scramble: "))
param = int(input("How long: "))
iterations = int(input("How many iterations would you like: "))
bool_val = int(input("Debug mode? 1: yes, 0: no "))
while bool_val != 1 and bool_val != 0:
    bool_val = int(input("Debug mode? 1: yes, 0: no "))
bound = 0
fails = 0


def scramble(scramble_str, param):
    scrambled = []
    for _ in range(len(scramble_str) * param):
        scrambled.append(scramble_str[randint(0, len(scramble_str) - 1)])
    return "".join(scrambled)


def checker(scramble_str, input_str):
    index = input_str.find(scramble_str)
    if index != -1:  # Changed from 1 to -1
        print(" \n \n Found!")
        print("The main string was this long: ", len(input_str))
        print("Substring found at this index: ", index)
        # print("Substring + or - 5 : ", input_str[max(0, index - 5):index + len(scramble_str) + 5])
        print("Substring + or - 5 : ", input_str[max(0, index - 5):index] + " " + input_str[index:index + len(scramble_str)] + " " + input_str[index + len(scramble_str):index + len(scramble_str) + 5] + "\n \n")
        return True
    else:
        return False


def __main__(bool_val):
    global bound, fails  # Accessing the global counters
    while bound <= iterations:
        try:
            # Scramble and check using the iterative scramble
            scrambled = scramble(scramble_str, param)
            if bool_val == 1:
                print(scrambled)
            found = checker(scramble_str, scrambled)

            if found:
                bound += 1
            else:
                fails += 1

            # Scramble and check using the recursive scramble
            if len(scramble_str * param) < 100:  # Arbitrary threshold for recursion
                scrambled_r = scramble(scramble_str, param)  # Reusing same logic for simplicity
                found_r = checker(scramble_str, scrambled_r)

                if found_r:
                    bound += 1
                else:
                    fails += 1

        except Exception as e:
            print(f":( {e}")

    print(f" \n It failed this number of times: {fails}")


__main__(bool_val)
