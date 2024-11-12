input_string = input("Enter a string: ")

def sentence_capitalizer(input_string):
    str_list = input_string.split(". ")
    for i in range(len(str_list)):
        str_list[i] += "."
        str_list[i] = str_list[i].capitalize()
    new_str =  " ".join(str_list)
    #this removes the dreaded extra period at the end of the string
    return new_str[:-1]
print(sentence_capitalizer(input_string))