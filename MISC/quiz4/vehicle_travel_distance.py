speed = int(input("What is the speed in MpH of the vehicle: "))
time = int(input("What is the time in hours: "))

iterator = 1

while iterator  <= time:
    print(f"Your vehicle has traveled {iterator * speed} miles in {iterator} hour(s).")
    iterator += 1