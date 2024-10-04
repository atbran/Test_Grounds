#This program creates a list and appends destinations to it.
#If the user types 'done', the program will print out the list of destinations.
destination = []

user_input = str(input("Please input the destination you would like to travel to: "))
print("Enter 'done' when you are finished.")

#casefold is used to allow any case to exist. IE input = DONE or DoNE or done, etc, they will be treated the same
while user_input.casefold() != "done":
    destination.append(user_input)
    user_input = str(input("Please input the destination you would like to travel to: "))

print(f"The following destinations have been added: {destination}")