from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.allrecipes.com/recipe/232420/pork-chop-skillet/").text
soup = BeautifulSoup(source,'lxml').prettify()
with open("copy_of_html.html","w") as file:
    file.write(soup)
