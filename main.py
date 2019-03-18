import mysql.connector
from scraping_details import *
# import json
# from recipe_reader import get_recipe_items

"""
to make a new mysql container
docker run --detach --name=test-mysql -v /home/hillash/Documents/SheCodes-Project/mysql-local:/var/lib/mysql --env="MYSQL_ROOT_PASSWORD=root" --publish 3306:3306 mysql

to run the mysql container
docker container start e2

to connect to the mysql container bash
docker exec -it e2 /bin/bash
"""

recipe_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Recipease"
)

cur = recipe_db.cursor()
# cur.execute("CREATE TABLE recipes (ID INTEGER AUTO_INCREMENT PRIMARY KEY, Ingredients VARCHAR(1000), Instructions TEXT, Total_Time VARCHAR(7), Servings TINYINT(2), Img_Name INT, Rating FLOAT);")
# cur.execute("ALTER TABLE recipes ADD Name VARCHAR(100);")
# cur.execute("ALTER TABLE recipes CHANGE COLUMN Name Name varchar(100) AFTER ID;")
# insert_command = "DROP TABLE recipes;"
# cur.execute(insert_command)
# insert_command = "INSERT INTO restrictions (Ingredient, Restriction_Type) VALUES (%s,%s);"
def iterate_recipes_into_db():
    with open("recipe_ids.txt","r") as file:
        recipe_ids = [x[:-2].replace("/","-") for x in file.readlines()]
    insert_command = "INSERT INTO recipes (Name, Ingredients, Instructions, Total_Time, Servings, Img_Name, Rating) VALUES (%s,%s,%s,%s,%d,%s,%.4f);"
    print(recipe_ids)
    recipe_details = []
    # for recipe in recipe_ids:
    #     recipe_details.append(((recipe),ingredients(recipe),instructions(recipe),total_time(recipe),serving(recipe),img_dl(recipe),rating(recipe)))
    # print(recipe_setails)
    # for i in x:
    #     print(type(i))
        # cur.execute(insert_command, recipe_details)

iterate_recipes_into_db()

recipe_db.commit()
