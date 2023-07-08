import config
import requests
from recipe import Recipes
from recipe_manager import RecipeManager
from web_manager import WebManager

R_ED_API_KEY = config.R_ED_API_KEY
R_APP_ID = config.R_APP_ID

# q=query text
# diet
# health
# type?
def is_valid_url(url):
    try:
        response = requests.head(url)
        return response.status_code >= 200 and response.status_code < 300
    except requests.exceptions.RequestException:
        return False

recipe_manager = RecipeManager()
web_manager = WebManager()

recipe_manager.intialise_db()
main_ingredient = input("Please list your main ingredients, separating with commas, or press enter to skip:")
diet = input("""Please enter ONE diet or press enter to skip.
Balanced                    Low-Carb
High-Fiber                  Low-Fat
High Protein                Low-Sodium
""").strip()

health = input("""Please input health requirement using commas to split, or press enter to skip.
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

type = input("""Please enter the type of meal you are looking for, press enter to skip.
Breakfast       Snack
Dinner          Teatime
Lunch

Your input: """).strip()

if main_ingredient == "" and diet == "" and health == "" and type == "":
    print("Please enter one requirement.")

q = ""
dietURL = ""
healthURL = ""
typeURL = ""

if main_ingredient != "":
    q = f"&q={main_ingredient}"
if diet != "":
    dietURL = f"&diet={diet}"
if health != "":
    healthURL = f"&health={health}"
if type != "":
    typeURL = f"&mealType={type}"

URL = f"https://api.edamam.com/api/recipes/v2?type=public{q}&app_id={R_APP_ID}&app_key={R_ED_API_KEY}{dietURL}{healthURL}{typeURL}"
response = requests.get(URL)
recipe_data = response.json()

recipe_list = recipe_data['hits']

for index, item in enumerate(recipe_list):
    url = item['recipe']['url']
    if not is_valid_url(url):
        recipe_list.pop(index)

for index, recipe in enumerate(recipe_list):
    recipe_name = recipe['recipe']['label']
    print(f"{index+1}. {recipe_name}")

choice = int(input("Enter the number of the recipe you want to choose: "))

# Retrieve the chosen recipe
chosen_recipe = recipe_list[choice - 1]['recipe']
url = chosen_recipe['url']


recipe_name = chosen_recipe['label']
ingredients = chosen_recipe['ingredientLines']
servings = chosen_recipe['yield']
calories_total = round(chosen_recipe['calories'])
calories_per_serving = round(calories_total/servings)

print(recipe_name)
for item in ingredients:
    print(item)
print(url)

print(calories_per_serving)

