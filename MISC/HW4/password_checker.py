#this program tests a user's password against a plaintext password
#the user will have 4 incorrect attempts to enter the correct password
num_tries = 0
password = "plaintextpassword"

input_password = input("Enter the password: ")

while input_password != password or num_tries >= 4:
    #increases counter
    num_tries += 1
    if num_tries >= 4:
        print("Too many incorrect passwords. Exiting...")
        #exits the loop
        break
    print("Incorrect password. Try again.")
    input_password = input("Enter the password: ")


if input_password == password:
    print("Access granted!")