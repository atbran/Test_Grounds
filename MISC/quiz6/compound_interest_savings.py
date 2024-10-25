present_value = float(input("input your present value: "))
interest_rate = float(input("input your MONTHLY interest rate as decimal: "))
months = int(input("input the number of months: "))

def compound_interest_savings(present_value, interest_rate, months):
    future_value = present_value * ((1 + interest_rate) ** months)
    return future_value
#I called the function inside the print(f"") statement to display the result
print(f"Your future value is: {compound_interest_savings(present_value, interest_rate, months):.2f}")