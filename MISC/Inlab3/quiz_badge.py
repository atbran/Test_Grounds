# Participants who answer at least 3 questions correctly receive a “Beginner” badge.
# Participants who answer at least 6 questions correctly receive an “Intermediate” badge.
# Participants who answer at least 9 questions correctly receive an “Expert” badge

answers = int(input("How many answers did you get correct? "))


print("You will receive these badges: ")
if answers >= 9:
    print("Expert")

if answers >= 6:
    print("Intermediate")

if answers >= 3:
    print("Beginner")

if answers <3:
    print("None")