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
    number_of_meals = 7
    breakfast_list = []
    lunch_list = []
    dinner_list = []
    length = 0

    while not valid_input:
        calorie_limit = input("Please input your daily calorie limit.")

        if not calorie_limit.isdigit():
            input("\nPlease enter a numerical value. Press enter to try again.\n")
        else:
            break

    breakfast_calories = round(calorie_limit*0.25)
    lunch_calories = round(calorie_limit*0.3)
    dinner_calories = round(calorie_limit*0.3)
    snack_calories = round(calorie_limit*0.15)


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

    mealSetter(breakfast_calories)


    # lunch_main_ingredient = input(
    #     "\n\nFor dinner please list your main ingredients, separating with commas, or press enter to skip: ")
    # dinner_main_ingredient = input(
    #     "\n\nFor breakfast please list your main ingredients, separating with commas, or press enter to skip: ")
    # snacks_main_ingredient = input(
    #     "\n\nFor snacks please list your main ingredients, separating with commas, or press enter to skip: ")



def mealSetter(meal_type, calories, diet, health):
    valid_input = False
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
            print(f"{days_left} days left.")

    for key, value in meal.items():
        meal_list = web_manager.searchCalories(key, diet, health, meal_type, calories)

        print(f"Following {meal_type} choices: ")
        for index, item in enumerate(meal_list):
            print(f"{index + 1} - {item['recipe']['label']}")

        while not valid_input:
            user_choice = input(
                f"\nPlease choose {value} {meal_type} meals, separating them by a comma. You can choose in any order: ").strip().replace(" ", "")

            user_meal = user_choice.split(",")

            if len(user_meal) != value:
                input(f"\nPlease enter {number_of_meals} meals. Press enter and try again.\n")
            else:
                break

        for item in user_meal:
            meals_week.append(meal_list[int(item) - 1])

        print("\nYou have chosen:")
        for item in meals_week:
            print(item['recipe']['label'])


mealSetter("dinner", 300, "", "keto-friendly")
