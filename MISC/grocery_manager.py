#
# (4 points) You are managing your weekly grocery shopping list. Write a
# program named grocery_manager.py to complete the following tasks:
# 1. Create a string variable called store_name that stores the name of
# your grocery store.
# 2. Print the first and last character of the string variable store_name. This
# must use string indexing to access the last character.
# 3. Create a list called groceries that contains the names of five items you
# need to buy.
# 4. Find and print the length of the third item in the groceries list.

store_name = "The Big Donut"
print(f"The store name is {store_name}. The first and last letters of the name are {store_name[0]} and {store_name[len(store_name)-1]}")

my_grocery_list = ["Chocolate_Donut","Strawberry_donut","Plain_Donut","50 Donut Holes", "Cinnamon_donut" ]


print(f"The name and length of the third item in my grocery list is: {my_grocery_list[2]} and {len(my_grocery_list[2])}.")
