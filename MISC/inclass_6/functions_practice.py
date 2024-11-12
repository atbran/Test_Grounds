#This program determines the speed of a vehicle or object and classifies it as slow or fast.
def speed_category(distance,time):
    speed = distance / time
    if speed < 60:
        return 'Slow'
    elif speed >= 60:
        return 'Fast'
    else:
        return 'Error'
#This is where the input is taken and the function is called.
km= float(input("Enter the distance in km: "))
hours = float(input("Enter the hours: "))
print(f"You are going {speed_category(km,hours)}!")
