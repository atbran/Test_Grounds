#This program prints out the even indexed chars of a string and then the string up to that index.
string_input = input("Enter a string: ")

def get_even_indexed_characters(string_input):
    for i in range(0, len(string_input), 2):
        print(f"{i} {string_input[i]} {string_input[:i+1]}")
get_even_indexed_characters(string_input)