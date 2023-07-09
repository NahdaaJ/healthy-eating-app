import config
import requests
from recipe import Recipes
from recipe_manager import RecipeManager
from web_manager import WebManager

R_ED_API_KEY = config.R_ED_API_KEY
R_APP_ID = config.R_APP_ID

recipe_manager = RecipeManager()
web_manager = WebManager()

def mainMenu():
    valid_input = False
    recipe_manager.initialise_db()

    while not valid_input:
        user_input = input("""Welcome to your Healthy Eating App!
        
1 - Find a new recipe
2 - View saved recipes
3 - Create a meal plan
4 - View past meal plans
5 - View current meal plan
6 - Exit

Your input: """).strip()

        match user_input:
            case "1":
                findRecipe()
            case other:
                input("Invalid input. Press enter to try again.\n")

def findRecipe():
    main_ingredient = input("\n\nPlease list your main ingredients, separating with commas, or press enter to skip:")

    diet = input("""\nPlease enter ONE diet or press enter to skip.
    Balanced                    Low-Carb
    High-Fiber                  Low-Fat
    High Protein                Low-Sodium
    """).strip()

    health = input("""\nPlease input health requirement using commas to split, or press enter to skip.
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

    type = input("""\nPlease enter the type of meal you are looking for, press enter to skip.
    Breakfast       Snack
    Dinner          Teatime
    Lunch
    
    Your input: """).strip()

    if main_ingredient == "" and diet == "" and health == "" and type == "":
        print("\nPlease enter one requirement.")

    try:
        recipe_list = web_manager.generateRecipe(main_ingredient, diet, health, type)
    except:
        input("\nNo hits found. Press enter to search again.")
        findRecipe()

    print("\n\n")
    for index, recipe in enumerate(recipe_list):
        recipe_name = recipe['recipe']['label']
        print(f"{index+1}. {recipe_name}")

    search_again = input("\nWould you like to search again? (Y/N)").strip().lower()

    if search_again == "y":
        findRecipe()

    choice = int(input("\nEnter the number of the recipe you want to choose: "))

    # Retrieve the chosen recipe
    chosen_recipe = recipe_list[choice - 1]['recipe']
    url = chosen_recipe['url']


    recipe_name = chosen_recipe['label'].title()
    ingredients = chosen_recipe['ingredientLines']
    servings = chosen_recipe['yield']
    calories_total = round(chosen_recipe['calories'])
    calories_per_serving = round(calories_total/servings)

    print("\n\n")
    print(f"""----------------{recipe_name}----------------
Servings: {servings}            Calories per Serving: {calories_per_serving}

INGREDIENTS:""")
    for item in ingredients:
        print(item)

    print(f"""Recipe URL: {url}
-------------------------------------------------------\n""")


    save_recipe = input("Would you like to save this recipe? (Y/N)").strip().lower()
    if save_recipe == "y":
        new_recipe = Recipes(recipe_name, url, ingredients, diet, health, calories_per_serving, servings)
        recipe_manager.add_recipe(new_recipe)

mainMenu()