from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
from import_export_file import output_file_path


def generate_links_list():
    links = []

    for page_count in range(1, 4):
        url = f'https://www.ewg.org/sunscreen/about-the-sunscreens/?&search=hawaiian+tropic&spage={page_count}'
        r = requests.get(url)
        soup = bs(r.content, "lxml")

        a = soup.find_all('a')
        for item in a:
            b = item.get('href')
            if "Hawaiian_Tropic" in b:
                links.append(b)
    return links


def scrape_ingredients(links_list):
    array = []

    for item in links_list:
        r = requests.get(item)
        soup = bs(r.content, "lxml")
        almost_ingredients = soup.find('div', class_="tyty2015_class_gages_col_individual tyty2015_class_zeropadding")
        ingredients_text = almost_ingredients.find('p').text
        ingredients_spaces = ingredients_text.replace('\n', '').strip()
        ingredients = re.sub('  +', '', ingredients_spaces)

        title = soup.find('title').text
        item_name = title.replace('EWG rating for ', '')
        item_name = item_name.replace("; | EWG's Guide to Sunscreens", '')

        ingredients_list = [item, item_name, ingredients]
        array.append(ingredients_list)

    df = pd.DataFrame(array, columns=['URL', 'Item Name', 'Ingredients'])
    return df


def main():
    output_csv_name = output_file_path()
    links_list = generate_links_list()
    df = scrape_ingredients(links_list)
    df.to_csv(output_csv_name)
    print('Export to CSV successful')


if __name__ == "__main__":
    main()
