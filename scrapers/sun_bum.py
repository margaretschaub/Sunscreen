from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
import docopt


def generate_links_list(url):
    links = []
    r = requests.get(url)
    soup = bs(r.content, "lxml")

    new_links = soup.find_all("p", class_="product-card__info-title")
    for each in new_links:
        a = each.contents[1]
        b = a.get('href')
        complete_url = 'https://www.sunbum.com/' + b
        links.append(complete_url)

    return links


def scrape_ingredients(links_list):
    array = []

    for item in links_list:
        r = requests.get(item)
        soup = bs(r.content, "lxml")
        almost_ingredients = soup.find_all('div', class_="product-detail__text")
        ingredients_text = almost_ingredients[2].text
        ingredients_spaces = ingredients_text.replace('\n', '').strip()
        ingredients = re.sub('  +', '', ingredients_spaces)

        almost_item_name = soup.find('title', class_="site-title").text
        item_name_spaces = almost_item_name.replace("\n", ' ').strip()
        item_name = re.sub('  +', '', item_name_spaces)

        ingredients_list = [item, item_name, ingredients]
        array.append(ingredients_list)

    df = pd.DataFrame(array, columns=['URL', 'Item Name', 'Ingredients'])
    return df


usage = ''' 
Usage: 
sun_bum.py [options] <name>

Arguments:
name     output csv file name

Options:
  -h --help           Show this screen.'''


def main():
    args = docopt.docopt(usage)
    initial_url = 'https://www.sunbum.com/collections/sun-care-all'
    links_list = generate_links_list(initial_url)
    df = scrape_ingredients(links_list)
    output = args['<name>']
    df.to_csv(output)
    print('Export to CSV successful')


if __name__ == "__main__":
    main()
