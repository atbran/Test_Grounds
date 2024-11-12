string_input = input("Enter numbers with no spaces: ")
total = 0
for i in range(len(string_input)):
    total += int(string_input[i])
print(total)

