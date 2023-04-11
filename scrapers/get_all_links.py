from bs4 import BeautifulSoup as bs
import requests
import json
from scrapers.foodland_store_id import get_store_id
from math import ceil


def create_list_of_links(starting_url):
    links = []
    foodland_store_id_list = get_store_id(starting_url)

    for retailer_store_id in foodland_store_id_list:
        url = f'https://shop.foodland.com/sm/pickup/rsid/{retailer_store_id}/results?q=sunscreen&page=1&skip=30'
        r = requests.get(url)
        soup = bs(r.content, "lxml")

        dictionary_raw = soup.find_all('script')
        located = dictionary_raw[1].text
        dictionary_sliced = located[27:]

        sunscreen_dict = json.loads(dictionary_sliced)
        total_item_count = sunscreen_dict['search']['pagination']['searchResults']['totalItems']
        item_per_page_count = sunscreen_dict['search']['pagination']['searchResults']['itemsPerPage']
        ceiling = ceil(total_item_count/item_per_page_count)

        if ceiling == 1:
            links.append(f'https://shop.foodland.com/sm/pickup/rsid/{retailer_store_id}'
                         f'/results?q=sunscreen&page=1&skip=0')
        elif ceiling == 2:
            links.append(f'https://shop.foodland.com/sm/pickup/rsid/{retailer_store_id}'
                         f'/results?q=sunscreen&page=1&skip=0')
            links.append(f'https://shop.foodland.com/sm/pickup/rsid/{retailer_store_id}'
                         f'/results?q=sunscreen&page=2&skip=30')
        else:
            links.append(f'https://shop.foodland.com/sm/pickup/rsid/{retailer_store_id}'
                         f'/results?q=sunscreen&page=1&skip=0')
            links.append(f'https://shop.foodland.com/sm/pickup/rsid/{retailer_store_id}'
                         f'/results?q=sunscreen&page=2&skip=30')
            links.append(f'https://shop.foodland.com/sm/pickup/rsid/{retailer_store_id}'
                         f'/results?q=sunscreen&page=3&skip=60')

    return links


if __name__ == "__main__":
    print(create_list_of_links('https://shop.foodland.com/sm/pickup/rsid/50/results?q=sunscreen&page=1&skip=0'))
