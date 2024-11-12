#this program checks if a phone number is valid

#allowed_chars = ["-",".","","0","1","2","3","4","5","6","7","8","9"]
#if len 14, must be 10 digits must have separators - or ., if len 11, first char must be 1, if len 12, must have separators - or .

def is_valid_phone_number(n):
    if len(n) == 10:
        for i in range(len(n)):
            #if not a num basically
            if not ('0' <= n[i] <= '9'):
                return False
        return True

    if len(n) == 11:
        #if length is 11, first char must be 1
        if n[0] != '1':
            return False
        for i in range(1, len(n)):

            if not ('0' <= n[i] <= '9'):
                return False
        return True

    if len(n) == 12:
        #if length is 12, it must have separators - or .
        separator = n[3]
        if separator not in '-.':
            return False
        if n[7] != separator:
            return False
        for i in range(len(n)):
            #check if not a num ignore the separators
            if i not in [3, 7]:
                if not ('0' <= n[i] <= '9'):
                    return False
        return True

    if len(n) == 14:
        if n[0] != '1':
            return False
        separator = n[1]
        if separator not in '-.':
            return False
        if n[1] != separator or n[5] != separator or n[9] != separator:
            return False
        for i in range(len(n)):
            # check if not a num ignore the separators
            if i not in [0, 1, 5, 9]:

                if not ('0' <= n[i] <= '9'):
                    return False
        return True

#otherwise false
    return False


print(is_valid_phone_number('1-800-867-5309'))
print(is_valid_phone_number('800.867.5309'))
print(is_valid_phone_number('8008675309'))
print(is_valid_phone_number('28008675309'))
print(is_valid_phone_number('800867530922'))
print(is_valid_phone_number('800*867*5309'))
print(is_valid_phone_number('800-867.5309'))
print(is_valid_phone_number('8oo-867-53o9'))
print(is_valid_phone_number('sloths are great'))