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

    print(f"\n\nYou have chosen a daily calorie limit of {calorie_limit}, with requirements '{diet}' and '{health}'.\nYour calories have been split as the following:")
    print(f"Breakfast Calories: {breakfast_calories}")
    print(f"Lunch Calories: {lunch_calories}")
    print(f"Dinner Calories: {dinner_calories}")
    print(f"Snack Calories: {snack_calories}")

    breakfast = mealPlanner("breakfast", breakfast_calories, diet, health)
    lunch = mealPlanner("lunch", lunch_calories, diet, health)
    dinner = mealPlanner("dinner", dinner_calories, diet, health)
    snack = mealPlanner("snack", snack_calories, diet, health)

    ingredientsCalculator(breakfast, lunch, dinner, snack,2)

def ingredientsCalculator(breakfast, lunch, dinner, snack, serving_size):
    meal_ingredients = {}

    for item in breakfast:
        serving = item['recipe']['yield']
        ingredients_multiplier = serving_size/serving

        for items in item['recipe']['ingredients']:
            quantity = str(round(items['quantity']*ingredients_multiplier, 2))
            if items['food'].lower() in meal_ingredients:
                if items['measure'] != "<unit>" and items['measure'] != None:
                    meal_ingredients[f"{items['food'].lower()}"] += ", " + quantity + " " + items['measure']
                else:
                    meal_ingredients[f"{items['food'].lower()}"] += ", " + quantity
            else:
                if items['measure'] != "<unit>" and items['measure'] != None:
                    meal_ingredients[f"{items['food'].lower()}"] = quantity + " " + items['measure']
                else:
                    meal_ingredients[f"{items['food'].lower()}"] = quantity

    for item in lunch:
        serving = item['recipe']['yield']
        ingredients_multiplier = serving_size/serving

        for items in item['recipe']['ingredients']:
            quantity = str(round(items['quantity']*ingredients_multiplier, 2))
            if items['food'].lower() in meal_ingredients:
                if items['measure'] != "<unit>" and items['measure'] != None:
                    meal_ingredients[f"{items['food'].lower()}"] += ", " + quantity + " " + items['measure']
                else:
                    meal_ingredients[f"{items['food'].lower()}"] += ", " + quantity
            else:
                if items['measure'] != "<unit>" and items['measure'] != None:
                    meal_ingredients[f"{items['food'].lower()}"] = quantity + " " + items['measure']
                else:
                    meal_ingredients[f"{items['food'].lower()}"] = quantity

    for item in dinner:
        serving = item['recipe']['yield']
        ingredients_multiplier = serving_size/serving

        for items in item['recipe']['ingredients']:
            quantity = str(round(items['quantity']*ingredients_multiplier, 2))
            if items['food'].lower() in meal_ingredients:
                if items['measure'] != "<unit>" and items['measure'] != None:
                    meal_ingredients[f"{items['food'].lower()}"] += ", " + quantity + " " + items['measure']
                else:
                    meal_ingredients[f"{items['food'].lower()}"] += ", " + quantity
            else:
                if items['measure'] != "<unit>" and items['measure'] != None:
                    meal_ingredients[f"{items['food'].lower()}"] = quantity + " " + items['measure']
                else:
                    meal_ingredients[f"{items['food'].lower()}"] = quantity

    for item in snack:
        serving = item['recipe']['yield']
        ingredients_multiplier = serving_size/serving

        for items in item['recipe']['ingredients']:
            quantity = str(round(items['quantity']*ingredients_multiplier, 2))
            if items['food'].lower() in meal_ingredients:
                if items['measure'] != "<unit>" and items['measure'] != None:
                    meal_ingredients[f"{items['food'].lower()}"] += ", " + quantity + " " + items['measure']
                else:
                    meal_ingredients[f"{items['food'].lower()}"] += ", " + quantity
            else:
                if items['measure'] != "<unit>" and items['measure'] != None:
                    meal_ingredients[f"{items['food'].lower()}"] = quantity + " " + items['measure']
                else:
                    meal_ingredients[f"{items['food'].lower()}"] = quantity

    print("\nIngredient List:")
    meal_ingredients = sorted(meal_ingredients.items())

    for key, value in meal_ingredients:
        print(f"{key.title()} - {value}")

    print("""Metric Conversions:
1 Ounce,oz =  28 Grams,g
1 Pound,lb = 0.45 Kilograms,kg""")

def mealPlanner(meal_type, calories, diet, health):
    valid_input = True
    days_left = 7
    meal = {}
    meals_week = []

    print(f"\n------------------------------------{meal_type.upper()}------------------------------------\n")
    while days_left > 0:
        main_ingredient = input(
            f"For {meal_type} please list your main ingredients, separating with commas, or press enter to skip: ")
        number_of_meals = input("How many days would you like this to be the main ingredient? ")

        if not number_of_meals.isdigit():
            input("\nPlease enter a numerical value. Press enter to try again.\n")
            continue

        if days_left-int(number_of_meals) < 0:
            print(f"You have {days_left} days left. Input too large.\n")
            continue
        else:
            meal[f'{main_ingredient}'] = int(number_of_meals)
            days_left -= int(number_of_meals)
            if days_left != 0:
                print(f"{days_left} days left.\n")

    for key, value in meal.items():
        meal_list = web_manager.searchCalories(key, diet, health, meal_type, calories)

        print(f"\nFollowing {meal_type} choices: ")
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