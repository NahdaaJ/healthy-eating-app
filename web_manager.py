import requests
import config

APP_ID = config.APP_ID
ED_API_KEY = config.ED_API_KEY

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
            calorie_URL = f"https://api.edamam.com/api/nutrition-data?app_id={APP_ID}&app_key={ED_PI_KEY}&ingr={item}"
            response = requests.get(calorie_URL)
            ingredient = response.json()
            calories += ingredient['calories']

        return calories

