from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = 'https://littlehandshawaii.com'
r = requests.get(url)
soup = bs(r.content, "lxml")

array = []
links = []
new_links = soup.find_all("div", class_="relative product_image")

for each in new_links:
    a = each.contents[1]
    b = a.get('href')
    completeurl = url + b
    links.append(completeurl)

for item in links:
    r = requests.get(item)
    soup = bs(r.content, "lxml")
    product_name = soup.title.text.strip()
    try:
        ingredients = soup.find('div', class_='sixteen columns rte').text
        ingredients_list = ingredients.split('\n')
        no_empty_string_list = [x for x in ingredients_list if x != '']
        new_list = [item, product_name, no_empty_string_list[1], no_empty_string_list[2]]
    except AttributeError:
        try:
            ingredients = soup.find('div', class_='product-block product-block--description').text
            ingredients_list = ingredients.split('\n')
            no_empty_string_list = [x for x in ingredients_list if x != '']
            new_list = [item, product_name, no_empty_string_list[9], no_empty_string_list[10]]
        except IndexError:
            ingredients = ''

    array.append(new_list)

df = pd.DataFrame(array, columns= ['URL', 'Item Name', 'Active Ingredients', 'Inactive Ingredients'])

df.to_csv(r'/Users/margaretschaub/Desktop/lhh.csv')



