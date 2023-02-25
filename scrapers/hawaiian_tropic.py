from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd

array = []
links = []
for page_count in range(1,4):
    url = f'https://www.ewg.org/sunscreen/about-the-sunscreens/?&search=hawaiian+tropic&spage={page_count}'
    r = requests.get(url)
    soup = bs(r.content, "lxml")
    new_links = soup.find_all('ul', class_="clearfix search_results_list")
    for each in new_links:
        a = soup.find_all('a')
        for item in a:
            c = item.get('href')
            if "Hawaiian_Tropic" in c:
                links.append(c)

for item in links:
    r = requests.get(item)
    soup = bs(r.content, "lxml")
    almost_ingredients = soup.find('div', class_ ="tyty2015_class_gages_col_individual tyty2015_class_zeropadding")
    c = almost_ingredients.find('p')
    ingredients_text = c.text
    ingredients_spaces = ingredients_text.replace('\n','').strip()
    ingredients = re.sub('  +', '', ingredients_spaces)

    title = soup.find('title').text
    item_name = title.replace('EWG rating for ','')
    item_name = item_name.replace("; | EWG's Guide to Sunscreens",'')

    ingredients_list = [item, item_name, ingredients]
    array.append(ingredients_list)

df = pd.DataFrame(array, columns= ['URL', 'Item Name', 'Ingredients'])
df.to_csv(r'/Users/margaretschaub/Desktop/hawaiian_tropic.csv')
