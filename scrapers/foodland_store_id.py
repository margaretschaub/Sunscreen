from bs4 import BeautifulSoup as bs
import requests
import json


def get_store_id(url):
    r = requests.get(url)
    soup = bs(r.content, "lxml")

    dictionary_raw = soup.find_all('script')
    located = dictionary_raw[2].text
    dictionary_sliced = located[27:]

    sunscreen_dict = json.loads(dictionary_sliced)
    product_card_dict = sunscreen_dict['search']['productCardDictionary']
    product_keys_list = [i for i in product_card_dict.keys()]
    store_dict = sunscreen_dict['stores']['availableDeliveryStores']['items']

    retailer_store_id_list = []
    for item in store_dict:
        retailer_store_id_list.append(item['retailerStoreId'])
    return retailer_store_id_list


