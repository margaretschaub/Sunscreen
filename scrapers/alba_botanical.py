from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd

url = 'https://www.albabotanica.com/?sfid=4326&_sf_s=sunscreen'
r = requests.get(url)
soup = bs(r.content, "lxml")

array = []
links = []
new_links = soup.find_all('h3', class_="cl-element cl-element-title cl-element--instance-1001")
for each in new_links:
    b = each.find('href')
    c = str(each)
    d = c.split('"')
    links.append(d[5])

for item in links:
    r = requests.get(item)
    soup = bs(r.content, "lxml")
    almost_ingredients = soup.find_all('div', id="ingredients")
    ingredients_text = almost_ingredients[0].text
    ingredients_spaces = ingredients_text.replace('\n','').strip()
    ingredients = re.sub('  +', '', ingredients_spaces)
    print(ingredients)
    item_name = soup.find('h2', class_="product-subtitle").text
    ingredients_list = [item, item_name, ingredients]
    array.append(ingredients_list)

df = pd.DataFrame(array, columns= ['URL', 'Item Name', 'Ingredients'])
df.to_csv(r'/Users/margaretschaub/Desktop/albabotanical.csv')

