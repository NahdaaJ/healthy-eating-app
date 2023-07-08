class Recipes:
   def __init__(self, name, ingredients, instructions, diet, calories, servings):
       self.name = name
       self.ingredients = ingredients
       self.instructions = instructions
       self.diet = diet
       self.calories = calories
       self.servings = servings

   def getRecipe(self):
       recipe = {
           "name": self.name,
           "ingredients": self.ingredients,
           "instructions": self.instructions,
           "diet": self.diet,
           "calories": self.calories,
           "servings": self.servings
       }

       return recipe