telephone_string = input("Enter a telephone number: ")

#Parse input by making it all uppercase
telephone_string = telephone_string.upper()

#To preface, this would be much easier to do with a dictionary. But I will do this instead because I do not want to be penalized.
for i in range(len(telephone_string)):
    if telephone_string[i] == "A" or telephone_string[i] == "B" or telephone_string[i] == "C":
        telephone_string = telephone_string.replace(telephone_string[i], "2")
    elif telephone_string[i] == "D" or telephone_string[i] == "E" or telephone_string[i] == "F":
        telephone_string = telephone_string.replace(telephone_string[i], "3")
    elif telephone_string[i] == "G" or telephone_string[i] == "H" or telephone_string[i] == "I":
        telephone_string = telephone_string.replace(telephone_string[i], "4")
    elif telephone_string[i] == "J" or telephone_string[i] == "K" or telephone_string[i] == "L":
        telephone_string = telephone_string.replace(telephone_string[i], "5")
    elif telephone_string[i] == "M" or telephone_string[i] == "N" or telephone_string[i] == "O":
        telephone_string = telephone_string.replace(telephone_string[i], "6")
    elif telephone_string[i] == "P" or telephone_string[i] == "Q" or telephone_string[i] == "R" or telephone_string[i] == "S":
        telephone_string = telephone_string.replace(telephone_string[i], "7")
    elif telephone_string[i] == "T" or telephone_string[i] == "U" or telephone_string[i] == "V":
        telephone_string = telephone_string.replace(telephone_string[i], "8")
    elif telephone_string[i] == "W" or telephone_string[i] == "X" or telephone_string[i] == "Y" or telephone_string[i] == "Z":
        telephone_string = telephone_string.replace(telephone_string[i], "9")


print(telephone_string)