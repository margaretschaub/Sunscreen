from bs4 import BeautifulSoup as bs
import requests
import json


def get_store_id(url):
    r = requests.get(url)
    soup = bs(r.content, "lxml")

    dictionary_raw = soup.find_all('script')
    located = dictionary_raw[1].text
    dictionary_sliced = located[27:]

    sunscreen_dict = json.loads(dictionary_sliced)
    store_dict = sunscreen_dict['stores']['availableDeliveryStores']['items']

    retailer_store_id_list = []
    for item in store_dict:
        retailer_store_id_list.append(item['retailerStoreId'])
    return retailer_store_id_list


def main():
    print(get_store_id('https://shop.foodland.com/sm/pickup/rsid/11/results?q=sunscreen'))


if __name__ == "__main__":
    main()
