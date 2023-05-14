from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from import_export_file import output_file_path


def generate_links_list(url):
    links = []
    r = requests.get(url)
    soup = bs(r.content, "lxml")

    new_links = soup.find_all("div", class_="relative product_image")
    for each in new_links:
        a = each.contents[1]
        b = a.get('href')
        complete_url = url + b
        links.append(complete_url)

    return links


def scrape_ingredients(links_list):
    array = []

    for item in links_list:
        r = requests.get(item)
        soup = bs(r.content, "lxml")
        try:
            almost_ingredients = soup.find('div', class_='sixteen columns rte').text

        except AttributeError:
            almost_ingredients = soup.find('div', class_='product-block product-block--description').text

        ingredients = almost_ingredients.replace('\n', ' ').strip()
        item_name = soup.title.text.strip()

        ingredients_list = [item, item_name, ingredients]
        array.append(ingredients_list)

    df = pd.DataFrame(array, columns=['URL', 'Item Name', 'Ingredients'])
    return df


def main():
    initial_url = 'https://littlehandshawaii.com'
    output_csv_name = output_file_path()
    links_list = generate_links_list(initial_url)
    df = scrape_ingredients(links_list)
    df.to_csv(output_csv_name)
    print('Export to CSV successful')


if __name__ == "__main__":
    main()
