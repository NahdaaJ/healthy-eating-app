# Daily calorie limit
# number of servings
# number of meals and their types
# main ingredient
# diet
# health

from web_manager import WebManager

web_manager = WebManager()

def generateMealPlan(number_of_meals, main_ingredients, diet, health, meal_type, calorie_limit):
    lunch_list = []
    length = 0

    breakfast_list = web_manager.searchCalories(main_ingredients, diet, health, meal_type, calorie_limit)


    print("Following lunch choices: ")
    for index, item in enumerate(breakfast_list):
        print(f"{index+1} - {item['recipe']['label']}")

    while length == 0:
        user_choice = input(f"Please choose {number_of_meals} lunches, separating them by a comma: ").strip().replace(" ", "")

        user_lunch = user_choice.split(",")

        if len(user_lunch) != number_of_meals:
            input(f"\nPlease enter {number_of_meals} meals. Press enter and try again.\n")
        else:
            break


    for item in user_lunch:
        lunch_list.append(breakfast_list[int(item)-1])

    for item in lunch_list:
        print(item['recipe']['label'])


def mealPlan():
    valid_input = False

    while not valid_input:
        calorie_limit = input("Please input your daily calorie limit: ")

        if not calorie_limit.isdigit():
            input("\nPlease enter a numerical value. Press enter to try again.\n")
        else:
            break

    breakfast_calories = round(int(calorie_limit)*0.25)
    lunch_calories = round(int(calorie_limit)*0.3)
    dinner_calories = round(int(calorie_limit)*0.3)
    snack_calories = round(int(calorie_limit)*0.15)

    print(f"Breakfast Calories: {breakfast_calories}")
    print(f"Lunch Calories: {lunch_calories}")
    print(f"Dinner Calories: {dinner_calories}")
    print(f"Snack Calories: {snack_calories}")


    diet = input("""\nFor your whole meal plan, please enter ONE diet or press enter to skip.
    Balanced                    Low-Carb
    High-Fiber                  Low-Fat
    High Protein                Low-Sodium

    Your Input: """).strip()

    health = input("""\nFor your whole meal plan, please input health requirement using commas to split, or press enter to skip.
    Alcohol-Free            Kosher                  Pork-Free
    Celery-Free             Low-Fat-Abs             Red-Meat-Free
    Crustacean-Free         Low-Sugar               Sesame-Free
    Dairy-Free              Lupine-Free             Shellfish-Free
    DASH                    Mediterranean           Soy-Free
    Egg-Free                Mollusk-Free            Sugar-Conscious
    Fish-Free               Mustard-Free            Sulfite-Free
    Fodmap-Free             No-Oil-Added            Tree-Nut-Free
    Gluten-Free             Paleo                   Vegan
    Immuno-Supportive       Peanut-Free             Vegetarian
    Keto-Friendly           Pescatarian             Wheat-Free

    Your input: """).strip()

    breakfast = mealPlanner("breakfast", breakfast_calories, diet, health)
    lunch = mealPlanner("lunch", lunch_calories, diet, health)
    dinner = mealPlanner("dinner", dinner_calories, diet, health)
    snack = mealPlanner("snack", snack_calories, diet, health)

    print("Breakfast:")
    for item in breakfast:
        print(item)

    print("\nLunch:")
    for item in lunch:
        print(item)

    print("\nDinner:")
    for item in dinner:
        print(item)

    print("\nSnacks:")
    for item in snack:
        print(item)


def mealPlanner(meal_type, calories, diet, health):
    valid_input = True
    days_left = 7
    meal = {}
    meals_week = []

    while days_left > 0:
        main_ingredient = input(
            f"\n\nFor {meal_type} please list your main ingredients, separating with commas, or press enter to skip: ")
        number_of_meals = input("How many days would you like this to be the main ingredient? ")

        if not number_of_meals.isdigit():
            input("\nPlease enter a numerical value. Press enter to try again.\n")
            continue

        if days_left-int(number_of_meals) < 0:
            print(f"You have {days_left} days left. Input too large.")
            continue
        else:
            meal[f'{main_ingredient}'] = int(number_of_meals)
            days_left -= int(number_of_meals)
            if days_left != 0:
                print(f"{days_left} days left.")

    for key, value in meal.items():
        meal_list = web_manager.searchCalories(key, diet, health, meal_type, calories)

        print(f"Following {meal_type} choices: ")
        for index, item in enumerate(meal_list):
            print(f"{index + 1} - {item['recipe']['label']}")

        while valid_input:
            valid_input1 = True
            user_choice = input(
                f"\nPlease choose {value} {meal_type} meals, separating them by a comma. You can choose in any order: ").strip().replace(" ", "")

            meal_list_index = user_choice.split(",")

            if len(meal_list_index) != value:
                input(f"\nPlease enter {value} meals. Press enter and try again.\n")
                continue

            for index in meal_list_index:
                if int(index) > len(meal_list) or int(index)-1 < 0:
                    input(f"You've input a number outside of the scope. Press enter to try again.")
                    valid_input1 = False
                    break

            if valid_input1:
                for item in meal_list_index:
                    meals_week.append(meal_list[int(item) - 1])
                break

        print("\nYou have chosen:")
        for item in meals_week:
            print(item['recipe']['label'])

    return meals_week

mealPlan()