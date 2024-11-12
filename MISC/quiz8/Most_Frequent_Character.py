from numpy import character

count_mystring = input("Enter a list of characters to count: ")

#parse input
count_mystring = count_mystring.lower()


#I think I may have to use a dictionary here. Please don't penalize.
character_count = {}
for i in range(len(count_mystring)):
    #there probably is a better way to do this.
    character_count[count_mystring[i]] = count_mystring.count(count_mystring[i])
    max_key = next(iter(character_count))
    for j in character_count:
        if character_count[j] > character_count[max_key]:
            max_key = j
print(f"{max_key} occurs most frequently in the string. It occurs {character_count[max_key]} times.")
