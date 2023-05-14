from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
from import_export_file import output_file_path


def generate_links_list(url):
    links = []
    r = requests.get(url)
    soup = bs(r.content, "lxml")

    new_links = soup.find_all('h3', class_="cl-element cl-element-title cl-element--instance-1001")
    for each in new_links:
        c = str(each)
        d = c.split('"')
        links.append(d[5])

    return links


def scrape_ingredients(links_list):
    array = []

    for item in links_list:
        r = requests.get(item)
        soup = bs(r.content, "lxml")
        almost_ingredients = soup.find_all('div', id="ingredients")
        ingredients_text = almost_ingredients[0].text
        ingredients_spaces = ingredients_text.replace('\n', '').strip()
        ingredients = re.sub('  +', '', ingredients_spaces)

        almost_item_name = soup.find('h2', class_="product-subtitle").text
        item_name = f" Alba {almost_item_name}"

        ingredients_list = [item, item_name, ingredients]
        array.append(ingredients_list)

    df = pd.DataFrame(array, columns=['URL', 'Item Name', 'Ingredients'])
    return df


def main():
    initial_url = 'https://www.albabotanica.com/?sfid=4326&_sf_s=sunscreen'
    output_csv_name = output_file_path()
    links_list = generate_links_list(initial_url)
    df = scrape_ingredients(links_list)
    df.to_csv(output_csv_name)
    print('Export to CSV successful')


if __name__ == "__main__":
    main()
