# This program uses Zeller’s congruence to determine the day of the week from a calendar day.

#Taking inputs from the user
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day of the month (1-31): "))
year = int(input("Enter the year: "))

while month < 1 or month > 12 or day < 1 or day > 31:
    print("Invalid input")
    month = int(input("Enter the month (1-12): "))
    day = int(input("Enter the day of the month (1-31): "))
    year = int(input("Enter the year: "))

# Adjust month and year if month is January or February
if month <= 2:
    #new variables created so that correct date is outputted
    month_adjusted = month + 12
    year_adjusted = year - 1
    #Otherwise, keep same month and year
else:
    month_adjusted = month
    year_adjusted = year

# K = year of the century
K = year_adjusted % 100
# J = century
J = year_adjusted // 100

# This is Zeller's formula
h = (day + (13 * ( month_adjusted + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7

# list of days
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Display the date and day
day_name = days[h]
print(f"{month}/{day}/{year} is a {day_name}")
