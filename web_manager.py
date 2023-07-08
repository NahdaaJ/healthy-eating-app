import requests
import config

N_APP_ID = config.N_APP_ID
N_ED_API_KEY = config.N_ED_API_KEY

# https://spoonacular.com/food-api/docs
# https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2
# diet string
# includeIngredients string
# type string
# instructionsRequired=true
# fillIngredients=true?
# addRecipeInformation=true?
# maxReadyTime string


# https://developer.edamam.com/edamam-docs-recipe-api
# https://api.edamam.com/api/recipes/v2?type=public&q=chicken,broccoli,garlic&app_id=YOUR_APP_ID&app_key=YOUR_APP_KEY
# q=query text
# diet
# health
# type?



class WebManager:

    def calculateCalories(self, ingredients):
        calories = 0

        for item in ingredients:
            calorie_URL = f"https://api.edamam.com/api/nutrition-data?app_id={N_APP_ID}&app_key={N_ED_API_KEY}&ingr={item}"
            response = requests.get(calorie_URL)
            ingredient = response.json()
            calories += ingredient['calories']

        return calories

    def generateRecipe(self):
        print("h")


