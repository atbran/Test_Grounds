#neccessary libraries
import random
import string

#variables for password strength calculations
high_bound = 12
med_bound = 8
low_bound = 6

#Get user preferences:
print("This is a password generator program. Please input necessary parameters as they are asked.")
pass_length = int(input("What length would you like your password to be? "))
pass_special_char_allowed = input("Would you like to use special characters? Y or N: ")
test_pass_Input = input("If you would like to test a password that has already been made, please enter it here: ")

def test_pass_check(test_pass):
    #password tester algo goes here!
    strength = 0
    if any(c.islower() for c in test_pass):
        strength += 1
    if any(c.isupper() for c in test_pass):
        strength += 1
    if any(c.isdigit() for c in test_pass):
        strength += 1
    if any(c in string.punctuation for c in test_pass):
        strength += 2
    if len(test_pass) >= high_bound:
        strength += 2
    elif len(test_pass) >= med_bound:
        strength += 1
    elif len(test_pass) <= low_bound:
        strength += -1
        print("Your password is too short!")
    else:
        print("Error!")
    #determine strength level
    if strength >= 5:
        return "Strong"
    elif 3 <= strength < 5:
        return "Moderate"
    else:
        return "Weak"

if test_pass_Input is not None:
    test_pass_check(test_pass_Input)
    password_strength = test_pass_check(test_pass_Input)
    print("Your password is considered:", password_strength)