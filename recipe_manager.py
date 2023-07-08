import config
import mysql.connector

database_name = "recipes"
table_name = "saved_recipes"

connection = mysql.connector.connect(
    host=config.HOST,
    user=config.USER,
    password=config.PASSWORD
)

cursor = connection.cursor()

class RecipeManager:
    def intialise_db(self):

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")

        connection.database = database_name

        cursor.execute(f"USE {database_name};")
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                            ID INT AUTO_INCREMENT PRIMARY KEY, 
                            name VARCHAR(255) NOT NULL,
                            ingredients TEXT NOT NULL,
                            instructions TEXT NOT NULL,
                            diet VARCHAR(255) NOT NULL,
                            calories_per_serving INT NOT NULL,
                            serving INT NOT NULL
                            );""")

        connection.commit()

        cursor.close()
        connection.close()

    def add_recipe(self, recipe):
        new_recipe = {
            "name": recipe.name,
            "ingredients": recipe.ingredients,
            "instructions": recipe.instructions,
            "diet": recipe.diet,
            "calories": recipe.calories,
            "servings": recipe.servings
        }

        insert_query = f"INSERT INTO {table_name} (name, ingredients, instructions, diet, calories_per_serving, serving) VALUES (%s, %s, %s, %s, %s, %s);"
        parameters = (new_recipe.name, new_recipe.ingredients, new_recipe.instructions, new_recipe.diet, new_recipe.calories, new_recipe.servings)

        cursor.execute(insert_query, parameters)
        connection.commit()

        cursor.close()
        connection.close()


