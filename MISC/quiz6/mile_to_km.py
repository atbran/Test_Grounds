
kilometers = float(input("Enter the number of miles: "))

def conversion(kilometers):
    miles = kilometers * .6214
    return miles

#I called the function inside the print(f"") statement to display the result
print(f"{kilometers} miles is equal to approximately {conversion(kilometers):.2f} kilometers.")