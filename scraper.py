from bs4 import BeautifulSoup as bs
import requests
import json
import pandas as pd


def get_info(product_key):
    product_specific_dict = product_card_dict[product_key]
    available = product_specific_dict['available']
    is_discounted = product_specific_dict['isDiscounted']
    brand = product_specific_dict['brand']
    name = product_specific_dict['name']
    price = product_specific_dict['price']
    sku = product_specific_dict['sku']
    label = product_specific_dict['unitOfSize']['label']
    size = product_specific_dict['unitOfSize']['size']
    try:
        unit_price = product_specific_dict['unitPrice']
    except KeyError:
        unit_price = ''
    was_price = product_specific_dict['wasPrice']

    if is_discounted is True:
        markdown = product_specific_dict['tprPrice']['markdown']
        markdown_label = product_specific_dict['tprPrice']['label']
        effective_from = product_specific_dict['tprPrice']['effectiveFrom']
        effective_until = product_specific_dict['tprPrice']['effectiveUntil']
        whole_price = product_specific_dict['tprPrice']['wholePrice']
    else:
        markdown = ''
        markdown_label = ''
        effective_from = ''
        effective_until = ''
        whole_price = ''

    product_info_list = [brand, sku, available, name, price, label, size, unit_price, was_price, is_discounted,
                         markdown, markdown_label, effective_from, effective_until, whole_price]

    return product_info_list


array = []
links = []
webpage_count = 2
num = 1
skip = 0
for x in range(webpage_count):
    url_form = f"https://shop.foodland.com/sm/pickup/rsid/11/results?q=sunscreen&page={num}&skip={skip}"
    # Need to make variable
    links.append(url_form)
    num += 1
    skip += 30

for url in links:
    r = requests.get(url)
    soup = bs(r.content, "lxml")

    dictionary_raw = soup.find_all('script')
    located = dictionary_raw[2].text
    dictionary_sliced = located[27:]

    sunscreen_dict = json.loads(dictionary_sliced)
    product_card_dict = sunscreen_dict['search']['productCardDictionary']
    product_keys_list = [i for i in product_card_dict.keys()]
    store_dict = sunscreen_dict['stores']['activeStoreDetails']
    name = store_dict['name']
    address_line1 = store_dict['addressLine1'].strip()
    address_line2 = store_dict['addressLine2']
    state = store_dict['countyProvinceState']
    post_code = store_dict['postCode']
    city = store_dict['city']
    longitude = store_dict['location']['longitude']
    latitude = store_dict['location']['latitude']
    store_id = [name, address_line1, address_line2, state, post_code, city, longitude, latitude]

    for item in product_keys_list:
        product_list = get_info(item)
        for each in store_id:
            product_list.append(each)

        array.append(product_list)


df = pd.DataFrame(array, columns=['Brand', 'sku', 'Available', 'Name', 'Price', 'Unit of Size',
                                  'Size', 'Price', 'Previous Price', 'Discounted', 'Markdown Price',
                                  'Markdown Label', 'Effective From', 'Effective Until', 'Whole Price',
                                  'Store', 'Island', 'Address', 'State', 'Zip', 'City', 'Longitude', 'Latitude'])

df.to_csv(r'/Users/margaretschaub/Desktop/foodlandsunscreen.csv')
