from recipe_scrapers import scrape_me
import mysql.connector
from scraping_details import img_dl, recipe_rating, recipe_serving
import mysql.connector

recipe_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Recipease"
)

cur = recipe_db.cursor()

with open('recipe_ids.txt', 'r') as file:
    content = file.readlines()
    for recipe_id in content:
        recipe_id = recipe_id[:-2]
        # scraper = scrape_me('http://allrecipes.com/recipe/'+recipe_id)
        with open('copy_of_html.html', 'r') as html:
            content = html.read()
            scraper = scrape_me(content)
        insert_command = "INSERT INTO recipes (Name, Ingredients, Instructions, Total_Time, Servings, Img_Name, Rating) VALUES (%s,%s,%s,%s,%d,%s,%f);"
        str_ingredients = "\n".join(scraper.ingredients())
        command_parameters = (scraper.title(),str_ingredients,scraper.instructions(),scraper.total_time(),recipe_serving(recipe_id),img_dl(recipe_id),recipe_rating(recipe_id))
        cur.execute(insert_command,command_parameters)
recipe_db.commit()
# print(scraper.title(),"\n",
# scraper.total_time(),"\n",
# scraper.ingredients(),"\n",
# scraper.instructions(),"\n",
# scraper.links())
