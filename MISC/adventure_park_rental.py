# You’ve started an adventure park where visitors are charged based on the total hours they book.
# The rental fee is $25 per hour. To celebrate this month, the park is offering a special promotion: a
# 20% discount on the total rental cost.
# Write a program named adventure_park_rental.py that reads user input for the number of
# hours they wish to book. Compute the total cost before applying the discount, the amount of the
# discount, and the final cost after applying the 20% discount. Store these values in variables and
# print them in a clear and formatted output.


rental_fee = 25

#20% discount is .8 of original price
discount_rate = .8

hours_input = int(input("How many hours do you wish to book? "))

total_cost = hours_input * rental_fee
discount_cost = (total_cost * float(discount_rate))

money_saved = total_cost - discount_cost
print(f"Total price is {total_cost:.2f}$ but the discounted price is {discount_cost:.2f}$")
print(f"You saved {money_saved:.2f} dollars.")
