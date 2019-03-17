import mysql.connector
# import json
# from recipe_reader import get_recipe_items

"""
docker run --detach --name=test-mysql -v /home/hillash/Documents/SheCodes-Project/mysql-local:/var/lib/mysql --env="MYSQL_ROOT_PASSWORD=root" --publish 3306:3306 mysql

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
# records = []
# with open("starter_recipes.json", "r") as json_file:
#     json_data = json.load(json_file)
# for k in json_data.keys():
#     name,ingredients,instructions=get_recipe_items(k)
#     values=(name,",\n".join(ingredients),instructions)
#     records.append(values)
# print(records)
# for record in records:
#     cur.execute(insert_command,record)


recipe_db.commit()
