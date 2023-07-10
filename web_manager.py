import requests
import config
import random

N_APP_ID = config.N_APP_ID
N_ED_API_KEY = config.N_ED_API_KEY
R_ED_API_KEY = config.R_ED_API_KEY
R_APP_ID = config.R_APP_ID

# https://spoonacular.com/food-api/docs
# https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2
# diet string
# includeIngredients string
# type string
# instructionsRequired=true
# fillIngredients=true?
# addRecipeInformation=true?
# maxReadyTime string

class WebManager:

    def calculateCalories(self, ingredients):
        calories = 0

        for item in ingredients:
            calorie_URL = f"https://api.edamam.com/api/nutrition-data?app_id={N_APP_ID}&app_key={N_ED_API_KEY}&ingr={item}"
            response = requests.get(calorie_URL)
            ingredient = response.json()
            calories += ingredient['calories']

        return calories

    def validURL(url):
        try:
            response = requests.head(url)
            return response.status_code >= 200 and response.status_code < 300
        except requests.exceptions.RequestException:
            return False

    def searchCalories(self, main_ingredient, diet, health, meal_type, calorie):
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
        if meal_type != "":
            typeURL = f"&mealType={meal_type}"
        calorieURL = f"&calories=200-{calorie}"

        URL = f"https://api.edamam.com/api/recipes/v2?type=public{q}&app_id={R_APP_ID}&app_key={R_ED_API_KEY}{dietURL}{healthURL}{typeURL}{calorieURL}"
        print(URL)
        response = requests.get(URL)
        recipe_data = response.json()

        recipe_list = recipe_data['hits']

        for index, item in enumerate(recipe_list):
            url = item['recipe']['url']
            if not WebManager.validURL(url):
                recipe_list.pop(index)

        return recipe_list
    def generateRecipe(self, main_ingredient, diet, health, type):
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
            if not WebManager.validURL(url):
                recipe_list.pop(index)

        return recipe_list

    def generateRandomRecipe(self, main_ingredient, diet, health, type):
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
        print(URL)
        response = requests.get(URL)
        recipe_data = response.json()

        recipe_list = recipe_data['hits']

        for index, item in enumerate(recipe_list):
            url = item['recipe']['url']
            if not WebManager.validURL(url):
                recipe_list.pop(index)


        random_id = random.randint(0, len(recipe_list)-1)
        recipe = recipe_list[random_id]['recipe']

        return recipe


