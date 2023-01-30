from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd


url = 'https://www.sunbum.com/collections/sun-care-all'
r = requests.get(url)
soup = bs(r.content, "lxml")

array = []
links = []
new_links = soup.find_all("p", class_="product-card__info-title")
for each in new_links:
    a = each.contents[1]
    b = a.get('href')
    completeurl = 'https://www.sunbum.com/'+ b
    links.append(completeurl)

for item in links:
    r = requests.get(item)
    soup = bs(r.content, "lxml")
    almost_ingredients = soup.find_all('div', class_="product-detail__text")
    ingredients = almost_ingredients[2]
    ingredients_text = ingredients.text
    ingredient_list = ingredients_text.split('\n')
    almost_item_name = soup.find('title',class_="site-title").text
    item_name_spaces = almost_item_name.replace("\n",'').strip()
    item_name = re.sub(' +','',item_name_spaces)
    try:
        ingredient_list_combined = [item, item_name, ingredient_list[0], ingredient_list[2]]
    except IndexError:
        ingredient_list_combined = [item, item_name, ingredient_list[0], '']

    array.append(ingredient_list_combined)

df = pd.DataFrame(array, columns= ['URL', 'Item Name', 'Active Ingredients', 'Inactive Ingredients'])

df.to_csv(r'/Users/margaretschaub/Desktop/sunbum.csv')