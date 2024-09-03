#neccessary libraries
import random
import string

#variables for password strength calculations
high_bound = 12
med_bound = 8
low_bound = 6

#Get user preferences:
print("This is a password generator program. Please input necessary parameters as they are asked.")
#Get user preferences:
print("This is a password generator program. Please input necessary parameters as they are asked.")
#convert input into an int to avoid errors for pass_length, also tests if input is an int
try:
    pass_length = int(input("What length would you like your password to be? "))
except ValueError:
    print("Please enter a valid number for the password length.")

pass_special_char_allowed = input("Would you like to use special characters? Y or N: ")
test_pass_Input = input("If you would like to test a password that has already been made, please enter it here: ")


#convert pass_special_char_allowed into all uppercase to avoid 'y' being flagged as false
pass_special_char_allowed.upper()
def generate_password(length, special_chars):
    #this defines the password using user parameters
    chars = string.ascii_letters + string.digits
    if special_chars == 'Y':
        chars+= string.punctuation

    #generate the password
    return ''.join(random.choice(chars) for _ in range(length))


def test_pass_check(test_pass):
    #set strength to zero
    strength = 0
    #each if statement determines if it fits the following criteria and then adds points
    #to strength if it fits the criteria.
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

#this determines if a password was entered for the password strength checker. If there is a password to be checked,
#it will run below.
if test_pass_Input:
    password_strength = test_pass_check(test_pass_Input)
    print("Your password is considered:", password_strength)

#runs the function
generated_password = generate_password(pass_length, pass_special_char_allowed)
#prints the result
print("Your generated password is: ", generated_password)