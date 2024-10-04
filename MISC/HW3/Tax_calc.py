

# This program takes an input (amount of money earned) and then outputs the effective tax rate from that input.

income = float(input("What was your 2023 income? "))

# Initialize tax vars
original_income = income  # Keep the original income so we can use it to calculate effective tax rate
tax_owed = 0
tax_bracket_details = []

#bracket vars

brack0 = 11000
brack1 = 44725
brack2 = 95375
brack3 = 182100
brack4 = 231250
brack5 = 578125


# Ensure correct input
while income < 0:
    print("Error: Income value must be positive")
    income = float(input("What was your 2023 income? "))
else:
    #bracket logic here
    if income <= brack0:
        tax_owed = income * 0.10
        tax_bracket_details.append(f"First $11000: ${tax_owed:.2f}")
    else:
        tax_owed += 11000 * 0.10
        tax_bracket_details.append(f"First $11000: ${11000 * 0.10:.2f}")

    if income > brack0 and income <= brack1:
        tax = (income - 11000) * 0.12
        tax_owed += tax
        tax_bracket_details.append(f"$11000 - $44725: ${tax:.2f}")
    elif income > 44725:
        tax = (44725 - 11000) * 0.12
        tax_owed += tax
        tax_bracket_details.append(f"$11000 - $44725: ${tax:.2f}")
    if income > brack1 and income <= brack2:
        tax = (income - 44725) * 0.22
        tax_owed += tax
        tax_bracket_details.append(f"$44725 - $95375: ${tax:.2f}")
    elif income > 95375:
        tax = (95375 - 44725) * 0.22
        tax_owed += tax
        tax_bracket_details.append(f"$44725 - $95375: ${tax:.2f}")

    if income > brack2 and income <= brack3:
        tax = (income - 95375) * 0.24
        tax_owed += tax
        tax_bracket_details.append(f"$95375 - $182100: ${tax:.2f}")
    elif income > 182100:
        tax = (182100 - 95375) * 0.24
        tax_owed += tax
        tax_bracket_details.append(f"$95375 - $182100: ${tax:.2f}")

    if income > brack3 and income <= brack4:
        tax = (income - 182100) * 0.32
        tax_owed += tax
        tax_bracket_details.append(f"$182100 - $231250: ${tax:.2f}")
    elif income > 231250:
        tax = (231250 - 182100) * 0.32
        tax_owed += tax
        tax_bracket_details.append(f"$182100 - $231250: ${tax:.2f}")

    if income > brack4 and income <= brack5:
        tax = (income - 231250) * 0.35
        tax_owed += tax
        tax_bracket_details.append(f"$231250 - $578125: ${tax:.2f}")
    elif income > 578125:
        tax = (578125 - 231250) * 0.35
        tax_owed += tax
        tax_bracket_details.append(f"$231250 - $578125: ${tax:.2f}")

    if income > brack5:
        tax = (income - 578125) * 0.37
        tax_owed += tax
        tax_bracket_details.append(f"Over $578125: ${tax:.2f}")

    for detail in tax_bracket_details:
        print(detail)

    # Print total tax owed and convert tax_owed to percentage
    print(f"\nTotal tax owed: ${tax_owed:.2f}")
    effective_tax_rate = (tax_owed / original_income) * 100 if original_income > 0 else 0
    print(f"Effective tax rate: {effective_tax_rate:.1f}%")
