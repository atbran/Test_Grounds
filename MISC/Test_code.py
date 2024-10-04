#hours = input("How many hours did you work?")
#wage = input("What is your hourly wage?")
#gross_pay = int(hours) * int(wage) * 52
#print(f"You were paid {gross_pay} this year.")


# p = 1
# L = 1
# n = 1
# m = (((p/1200)*(1+(p/1200))**n)/(1+(p/1200)**n-1)*L)
#
# print(m)
#
# x = 1
# a = 1
# y = ((x+x**3)/(a*x**4)+(x+2*x**3)/(3*x-x**4)**5)
# print(y)


future_value = float(input("Enter your future value: "))
rate = float(input("Enter your rate: "))
years = int(input("Enter your years: "))
present_value = future_value/((1*rate)**years)

print("Deposit this amount: ", present_value)