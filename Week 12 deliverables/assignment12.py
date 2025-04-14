"""
Aaron Eberly
April 10, 2025
To be completely honest, I did not use any copilot or even a google search to write this code.
I pretty much wrote the same thing as my paper code, but with less errors due to the convenience of typing.
"""

def addMeal(newMeal, mealList):
    # This function adds a meal to the list
    mealList.append(newMeal)
    print("Meal added!")
    return mealList

def removeMeal(mealIndex, mealList):
    # This function removes a meal from the list
    del mealList[mealIndex]
    print("Meal removed!")
    return mealList

def displayMeals(mealList):
    # This function neatly prints all the meals and their info
    print("Meal\t\t\tCost\tCalories")
    for meal in mealList:
        for info in meal:
            print(info, end = "\t")
        print("")
    print("")

def findKeyIngredient(mealList, keyIngredient):
    searchedList = []
    # All meals with the key ingredient will be added to this list
    print(f"Searching for meals with {keyIngredient}...")
    try:
        for meal in mealList:
            pos = meal[0].find(keyIngredient.lower())
            if pos != -1:
                searchedList.append(meal)
        if len(searchedList) == 0:
            raise ValueError
        displayMeals(searchedList)
        # Display all the meals that were found
    except ValueError:
        print("The key ingredient could not be found.")


def main():
    # because mealList is a list, but the items within are tuples, meals can be added or removed, but the meals themselves can't be changed
    mealList = [("butterburger and fries", 8.00, 200), ("3 piece cod dinner", 18.20, 220), ("chicken and fries", 10.50, 160), ("pot roast sandwich", 7.50, 120), ("cheese curds and fries", 6.00, 100), ("crispy chicken sandwich", 9.00, 110), ("Kids meal with fries", 6.72, 90)]
    displayMeals(mealList)
    mealList = addMeal(("chicken noodle soup", 7.44, 80), mealList)
    displayMeals(mealList)
    mealList = removeMeal(1, mealList)
    displayMeals(mealList)
    findKeyIngredient(mealList, "Fries")
    # Uppercase or lowercase won't matter because the search function uses .lower()
    findKeyIngredient(mealList, "cod")
    # Will raise a ValueError because the only meal with cod was deleted

main()

