from bs4 import BeautifulSoup
import requests
import urllib


filepath = "/home/hillash/Documents/SheCodes-Project/"

def get_whole_html(recipe_id):
    filename = recipe_id[:-2].replace("/","-")
    urllib.request.urlretrieve("https://www.allrecipes.com/recipe/"+recipe_id, "/home/hillash/Documents/SheCodes-Project/html_pages/"+filename+".html")

def title(recipe_id):
    soup = BeautifulSoup(open(filepath+"html_pages/"+recipe_id+".html"), "lxml")
    title = soup.find('section', { 'class' : 'recipe-summary clearfix' }).h1.text
    return title

def total_time(recipe_id):
    soup = BeautifulSoup(open(filepath+"html_pages/"+recipe_id+".html"), "lxml")
    total_time = soup.find('span', { 'class' : 'ready-in-time' }).text
    return total_time

def img_dl(recipe_id):
# add recipe img to the local directory
    # source = requests.get("https://www.allrecipes.com/recipe/"+recipe_id).text
    # soup = BeautifulSoup(source,'lxml')
    soup = BeautifulSoup(open(filepath+"html_pages/"+recipe_id+".html"), "lxml")
    img_link = soup.find('div', { "class" : "hero-photo__wrap" }).a.img['src']
    img_name = list(img_link.split("/"))[5].split(".")[0]
    urllib.request.urlretrieve(img_link, filepath+"img/"+img_name+".jpg")
    return img_name

def ingredients(recipe_id):
    soup = BeautifulSoup(open(filepath+"html_pages/"+recipe_id+".html"), "lxml")
    ingredients = []
    ingredient_box = soup.find('div', { 'id' : 'polaris-app' })
    for ingredient in ingredient_box.find_all('li', { 'class' : 'checkList__line' }):
        ingredients.append(ingredient.label.span.text)
    return "\n".join(ingredients[:-3])

def instructions(recipe_id):
    soup = BeautifulSoup(open(filepath+"html_pages/"+recipe_id+".html"), "lxml")
    steps = []
    for step in soup.find_all('li', { 'class' : 'step' }):
        steps.append(step.span.text.strip())
    return "\n".join(steps[:-1])

def rating(recipe_id):
# get recipe rating
    # source = requests.get("https://www.allrecipes.com/recipe/"+recipe_id).text
    # soup = BeautifulSoup(source,'lxml')
    soup = BeautifulSoup(open(filepath+"html_pages/"+recipe_id+".html"), "lxml")
    recipe_rating = soup.find('div', { "class" : "recipe-summary__stars" }).div['data-ratingstars']
    return float(recipe_rating)

def serving(recipe_id):
# get recipe serving
    # source = requests.get("https://www.allrecipes.com/recipe/"+recipe_id).text
    # soup = BeautifulSoup(source,'lxml')
    soup = BeautifulSoup(open(filepath+"html_pages/"+recipe_id+".html"), "lxml")
    recipe_serving = soup.find('span',{ "class" : "recipe-ingredients__header__toggles" }).meta['content']
    return int(recipe_serving)

def download_html():
    with open('recipe_ids.txt','r') as file:
        recipe_ids = file.readlines()
    for recipe in recipe_ids:
        get_whole_html(recipe)


# def iterate_pages():
#     with open("recipe_ids.txt","r") as file:
#         recipe_ids = [x[:-2].replace("/","-") for x in file.readlines()]
#     for recipe in recipe_ids:
#         x = (title(recipe),ingredients(recipe),total_time(recipe),instructions(recipe),rating(recipe),serving(recipe))
#
#     print(x)
    # for recipe in recipe_ids:


# iterate_pages()
# total_time("232420-pork-chop-skillet")
