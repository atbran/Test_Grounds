print("Reboot the computer and try to connect.")
question = input("Did that fix the problem? {y/n} ")
question.lower()
if question == "y" or question == "yes" or question == "yes":
    print("Connection has been fixed.")
else:
    print("Reboot the router and try to connect")
    question = input("Did that fix the problem? {y/n} ")
    question.lower()
    if question == "y" or question == "yes":
        print("Connection has been fixed.")
    else:
        print("Make sure the cables between the router and modem are plugged in firmly.")
        question = input("Did that fix the problem? {y/n} ")
        question.lower()
        if question == "y" or question == "yes":
            print("Connection has been fixed.")
        else:
            print("Move the router to a new location and try to connect.")
            question = input("Did that fix the problem? {y/n} ")
            question.lower()
            if question == "y" or question == "yes":
                print("Connection has been fixed.")
            else:
                print("Get a new router.")