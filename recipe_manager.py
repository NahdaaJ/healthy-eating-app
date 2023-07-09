import config
import mysql.connector

database_name = "recipes"
table_name = "saved_recipes"

class RecipeManager:
    def initialise_db(self):
        connection = mysql.connector.connect(
            host=config.HOST,
            user=config.USER,
            password=config.PASSWORD,
        )

        cursor = connection.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name};")
        cursor.execute(f"USE {database_name};")
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
                           ID INT AUTO_INCREMENT PRIMARY KEY, 
                           name VARCHAR(255) NOT NULL,
                           url TEXT NOT NULL,
                           ingredients TEXT NOT NULL,
                           diet VARCHAR(255),
                           health VARCHAR(255),
                           calories_per_serving INT NOT NULL,
                           serving INT NOT NULL
                           );""")
        connection.commit()

        cursor.close()
        connection.close()

    def add_recipe(self, recipe):
        connection = mysql.connector.connect(
            host=config.HOST,
            user=config.USER,
            password=config.PASSWORD,
            database=database_name
        )
        cursor = connection.cursor()

        new_recipe = {
            "name": str(recipe.name),
            "url": str(recipe.url),
            "ingredients": str(recipe.ingredients),
            "diet": str(recipe.diet),
            "health": str(recipe.health),
            "calories": recipe.calories,
            "servings": recipe.servings
        }

        insert_query = f"INSERT INTO {table_name} (name, url, ingredients, diet, health, calories_per_serving, serving) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        parameters = (
            new_recipe['name'],
            new_recipe['url'],
            new_recipe['ingredients'],
            new_recipe['diet'],
            new_recipe['health'],
            new_recipe['calories'],
            new_recipe['servings']
        )

        cursor.execute(insert_query, parameters)
        connection.commit()

        cursor.close()
        connection.close()