# Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
# Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
# Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
# Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten- Free: No
# The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes

vegetarian = input("Is anyone in your party a Vegetarian? {y/n}")
vegan = input("Is anyone in your party a Vegan? {y/n}")
gluten_free = input("Is anyone in your party Gluten free? {y/n}")

vegetarian.lower()
vegan.lower()
gluten_free.lower()


print("Your resturant choices are: ")
if vegetarian != "y"  and vegan != "y" and gluten_free != "y" :
    print("Joe’s Gourmet Burgers \n Main Street Pizza Company  \n Corner Café—Vegetarian \n Mama’s Fine Italian \n The Chef’s Kitchen \n")

elif vegetarian == "y" and vegan != "y"  and gluten_free != "y" :
    print("Main Street Pizza Company  \n Corner Café—Vegetarian \n Mama’s Fine Italian \n The Chef’s Kitchen \n")

elif vegetarian == "y"  and vegan == "y"  and gluten_free != "y":
    print("Main Street Pizza Company \n Corner Café \n The Chef’s Kitchen \n")
elif vegetarian == "y"  and vegan != "y" and gluten_free == "y":
    print("Main Street Pizza Company \n Corner Café \n The Chef’s Kitchen \n")
elif vegetarian == "y"  and vegan == "y" and gluten_free == "y":
    print("Corner Cafe \n The Chef's Kitchen")
else:
    "error!"

