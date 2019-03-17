# from recipe_scrapers import scrape_me
from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.allrecipes.com/recipes/94/soups-stews-and-chili/").text
soup = BeautifulSoup(source,'lxml')

# add recipe id's to the list if they are not currently in it
with open('recipe_ids.txt','r+') as file:
    content = file.read()
    for article in soup.find_all('article', class_='fixed-recipe-card'):
        recipe_link = article.find('div', class_='fixed-recipe-card__info').h3.a['href']
        recipe_id = "/".join(recipe_link.split("/")[4:6])+"/"
        """
        recipe_id_filename = recipe_id[:-1].replace("/","-")
        """
        if recipe_id not in content:
            #file.write(recipe_id+"\n") #<- or should it be formatted for the filename?





"""
From JSON dataset
"""
# import json
#
# def get_recipe_items(recipe_id):
#     with open("starter_recipes.json", "r") as json_file:
#         json_data = json.load(json_file)
#     return json_data[recipe_id]["title"],json_data[recipe_id]["ingredients"],json_data[recipe_id]["instructions"]
