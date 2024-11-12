

def __main__(NUM_EMPLOYEE, HoursWorked, PayRate):
    HoursWorked = []
    PayRate = []
    gross_pay = []
    for i in range(NUM_EMPLOYEE):
        HoursWorked[i] = float(input("Enter the number of hours worked by employee {}: ".format(i + 1)))

    payRate = float(input("Enter the hourly pay rate for each employee: "))

    for i in range(NUM_EMPLOYEE):
        gross_pay[i] = HoursWorked[i] * PayRate[i]
    print(gross_pay)
