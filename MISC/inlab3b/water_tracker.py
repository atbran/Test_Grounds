#this program takes input from the user to determine how many cups of water they drank
#depending on the cups of water consumed, it will output a motivational message.

water_cups_consumed = int(input("How many cups of water have you drank today? "))
message = ""


if water_cups_consumed >= 8:
    message = "Excellent! You're well-hydrated."
elif water_cups_consumed >= 5:
    message = "Good! Keep it up, but try to drink more."
elif water_cups_consumed >= 2:
    message = "Warning! You should drink more water."
else:
    message = "Danger! You're severely dehydrated."

print(message)