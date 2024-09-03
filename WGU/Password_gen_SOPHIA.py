#neccessary libraries
import random
import string

#Get user preferences:
print("This is a password generator program. Please input necessary parameters as they are asked.")
pass_length = input("What length would you like your password to be? ")
pass_special_char_allowed = input("Would you like to use special characters? ")
test_pass = input("If you would like to test a password already made, please enter it here: ")

def test_pass_check(test_pass):
    #password tester algo goes here!
    strength = 0
    if any(c.islower() for c in test_pass):
        strength += 1
    pass
