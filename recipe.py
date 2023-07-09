class Recipes:
   def __init__(self, name, url, ingredients, diet, health, calories, servings):
       self.name = name
       self.url = url,
       self.ingredients = ingredients
       self.diet = diet
       self.health = health
       self.calories = calories
       self.servings = servings

   def getRecipe(self):
       recipe = {
           "name": self.name,
           "url": self.url,
           "ingredients": self.ingredients,
           "diet": self.diet,
           "health": self.health,
           "calories": self.calories,
           "servings": self.servings
       }

       return recipe
