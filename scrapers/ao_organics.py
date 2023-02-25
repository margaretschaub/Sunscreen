from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = 'https://www.aoorganicshawaii.com/collections/sunscreen'
r = requests.get(url)
soup = bs(r.content, "lxml")

array = []
links = []
new_links = soup.find_all("a", class_="product-link")

for each in new_links:
    a = each.get('href')
    completeurl = "https://www.aoorganicshawaii.com" + a
    if completeurl not in links:
        links.append(completeurl)
print(links)
for item in links:
    r = requests.get(item)
    soup = bs(r.content, "lxml")
    product_name = soup.title.text.strip()
    ingredients = soup.find('div', class_='product-description user-content container cf padded-row').text
    ingredients_list = ingredients.split('\n')
    no_empty_string_list = [x for x in ingredients_list if x != '']
    no_empty_string_list.insert(0, product_name)


