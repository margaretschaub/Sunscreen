from bs4 import BeautifulSoup as bs
import pandas as pd
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
        retailer_store_id = item['retailerStoreId']
        name = item['name']
        address_line1 = item['addressLine1'].strip().replace(":", "")
        address_line2 = item['addressLine2']
        state = item['countyProvinceState']
        post_code = item['postCode']
        city = item['city']
        longitude = item['location']['longitude']
        latitude = item['location']['latitude']
        coordinate = longitude,latitude
        store_id = [retailer_store_id, name, address_line1, address_line2, state, post_code, city, coordinate]
        retailer_store_id_list.append(store_id)

    df = pd.DataFrame(retailer_store_id_list, columns=['retailer_store_id','store_name','address_line1','address_line2',
                                                       'state','post_code', 'city', 'coordinate'])

    df.to_csv(r'/Users/margaretschaub/Desktop/foodland_store_details.csv')


if __name__ == "__main__":
    print(get_store_id('https://shop.foodland.com/sm/pickup/rsid/11/results?q=sunscreen'))