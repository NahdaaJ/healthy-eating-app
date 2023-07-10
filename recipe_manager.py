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
                           serving INT NOT NULL,
                           meal_type VARCHAR(255) NOT NULL
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
            "servings": recipe.servings,
            "meal_type": recipe.type
        }

        insert_query = f"INSERT INTO {table_name} (name, url, ingredients, diet, health, calories_per_serving, serving, meal_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        parameters = (
            new_recipe['name'],
            new_recipe['url'],
            new_recipe['ingredients'],
            new_recipe['diet'],
            new_recipe['health'],
            new_recipe['calories'],
            new_recipe['servings'],
            new_recipe['meal_type']
        )

        cursor.execute(insert_query, parameters)
        connection.commit()

        cursor.close()
        connection.close()

#     def searchDB(self, search_parameters):
#         connection = mysql.connector.connect(
#             host=config.HOST,
#             user=config.USER,
#             password=config.PASSWORD,
#             database=database_name
#         )
#         cursor = connection.cursor()
#         #search parameters = {
#
#
#         query = f"""SELECT * FROM {table_name}
# WHERE (calories_per_serving <= %s)
# AND (meal_type COLLATE utf8_general_ci LIKE %s)
# """
#         if not search_parameters.name == "":
#             query += f"AND (name COLLATE utf8_general_ci LIKE %s)"
#
#         if not search_parameters.diet == "":
#             query += f"AND (diet COLLATE utf8_general_ci LIKE %s)"
#
#         if not search_parameters.health == "":
#             query += f"AND (health COLLATE utf8_general_ci LIKE %s)"
#
#
#         max_calories = f"%{search_parameters.calories}%"  # Add wildcards to search term
#
#         params = (search_term, search_term, search_term, search_term, max_calories)
#
#         cursor.execute(query, params)
#         results = cursor.fetchall()
