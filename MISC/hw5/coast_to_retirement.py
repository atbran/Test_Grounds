#program calculates how many years until you can retire based on the idea of "coasting"


#this does the input validation and gets the vars
#normally I would use try catch blocks to make sure the input for types are correct but for the purpose
# of the assignment I will just use this
while True:
        current_age = int(input("What is your current age? "))
        if current_age < 0:
            print("Age cannot be negative.")
            continue

        starting_balance = float(input("What is your starting balance? "))
        if starting_balance < 0:
            print("Starting balance cannot be negative.")
            continue

        retirement_age = int(input("What is your retirement age? "))
        if retirement_age <= current_age:
            print("Retirement age must be greater than current age.")
            continue

        target_balance = float(input("What is your target balance? "))
        if target_balance <= starting_balance:
            print("Target balance must be greater than starting balance.")
            continue

        yearly_contribution = float(input("What is your yearly contribution? "))
        if yearly_contribution < 0:
            print("Yearly contribution cannot be negative.")
            continue

        growth_rate = float(input("What is your growth rate? "))
        if growth_rate < 0:
            print("Growth rate cannot be negative.")
            continue
        break

#this does the calculations and this is the variable that makes sure the loop stops and ends correctly
target_reached = False

for stopping_age in range(current_age, retirement_age + 1):
    balance = starting_balance
    age = current_age
    while age < stopping_age:
        growth = balance * growth_rate / 100
        balance = balance + growth + yearly_contribution
        age += 1

    while age < retirement_age:
        growth = balance * growth_rate / 100
        balance = balance + growth
        age += 1

    if balance >= target_balance:
        target_reached = True
        print(f"\nYou can stop contributing at age {stopping_age}")

        balance = starting_balance
        age = current_age

        print("\nYear by year projection:")
        while age < stopping_age:
            growth = balance * growth_rate / 100
            old_balance = balance
            balance = balance + growth + yearly_contribution
            print(f"Age {age}: ${old_balance:.2f} to ${balance:.2f} (growth: ${growth:.2f}, contribution: ${yearly_contribution:.2f})")
            age += 1


        while age < retirement_age:
            growth = balance * growth_rate / 100
            old_balance = balance
            balance = balance + growth
            print(f"Age {age}: ${old_balance:.2f} to ${balance:.2f} (growth: ${growth:.2f}, no contribution)")
            age += 1
        print(f"\nFinal balance at retirement: ${balance:.2f}")
        break

if not target_reached:
    print("\nTarget balance cannot be reached with the given parameters.")