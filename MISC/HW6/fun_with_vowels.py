#This code determines the number of vowels in the string and the number of syllables.

vowels = ["a", "e", "i", "o", "u"]

def vowel_count(str_input):
    vowel_count = 0
    for i in range(len(str_input)):
        #I dont know if this is allowed but using 'in' is the simplest way to do this.
        if str_input[i] in vowels:
            vowel_count += 1
    return vowel_count

#I do not like using one letter var names for a parameter but that is what the assignment says.
# w = input string
def count_syllables(W):
    syllable_count = 0
    #If starts with vowel, increment
    if len(W) > 0 and W[0] in vowels:
        syllable_count += 1

    for i in range(1, len(W)):
        if W[i] in vowels and W[i - 1] not in vowels:
            syllable_count += 1

    return syllable_count

#test cases
print("Cheeseburger " + str(vowel_count("Cheeseburger")))
print("Hot dog " + str(vowel_count("Hot dog")))
print("Hamburger " + str(vowel_count("Hamburger")))
print("Pizza " + str(vowel_count("Pizza")))
print("Cheeseburger syllables: " + str(count_syllables("Cheeseburger")))
print("Hot dog syllables: " + str(count_syllables("Hot dog")))
print("Hamburger syllables: " + str(count_syllables("Hamburger")))
print("Pizza syllables: " + str(count_syllables("Pizza")))

#required test cases
print(vowel_count(''))        # Expected: 0

print(vowel_count('Z'))  # Expected: 0
print(vowel_count('sloth'))   # Expected: 1
print(vowel_count('SlOTh'))   # Expected: 1
print(vowel_count('slothy'))  # Expected: 1
print(vowel_count('ABACUS'))  # Expected: 3

print(count_syllables(''))        # Expected: 0
print(count_syllables('Z'))       # Expected: 0
print(count_syllables('i'))       # Expected: 1
print(count_syllables('OWL'))    # Expected: 1
print(count_syllables('tomato'))  # Expected: 3
print(count_syllables('write'))    # Expected: 2