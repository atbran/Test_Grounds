fat_grams = float(input("Enter the number of fat grams: "))
carb_grams = float(input("Enter the number of carb grams: "))

def calories_from_fat(fat_grams):
    fat_calories = fat_grams * 9
    return fat_calories

def calories_from_carbs(carb_grams):
    carb_calories = carb_grams * 4
    return carb_calories

#I called the function inside the print(f"") statement to display the result
print(f"You have these calories from fat: {calories_from_fat(fat_grams):.2f} and these calories from carbs: {calories_from_carbs(carb_grams):.2f}")
#I called the function inside the print(f"") statement to display the result
print(f"Total calories: {calories_from_fat(fat_grams) + calories_from_carbs(carb_grams):.2f}")