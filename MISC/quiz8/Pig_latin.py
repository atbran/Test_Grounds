#English: I SLEPT MOST OF THE NIGHT
# Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY

english_input = input("Enter a sentence: ")
words = english_input.split()

pig_latin_array = []

def pig_latin_func(word):
    for i in word:
        #take first letter out, add it to the end, and add "AY" then a space
        pig_latin_array.append(i[1:] + i[0] + "AY" + " ")
    return "".join(pig_latin_array)

print(pig_latin_func(words))
