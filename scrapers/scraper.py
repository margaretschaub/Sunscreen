from bs4 import BeautifulSoup as bs
import requests
import json
import pandas as pd

from get_all_links import create_list_of_links
import docopt


def export_csv(links, output_file):
    array = []

    for url in links:
        r = requests.get(url)
        soup = bs(r.content, "lxml")

        dictionary_raw = soup.find_all('script')
        located = dictionary_raw[1].text
        dictionary_sliced = located[27:]

        sunscreen_dict = json.loads(dictionary_sliced)
        product_card_dict = sunscreen_dict['search']['productCardDictionary']
        product_keys_list = [i for i in product_card_dict.keys()]
        store_dict = sunscreen_dict['stores']['activeStoreDetails']
        retailer_store_id = store_dict['retailerStoreId']

        for item in product_keys_list:
            product_specific_dict = product_card_dict[item]
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

            product_list = [brand, sku, available, name, price, label, size, unit_price, was_price, is_discounted,
                            markdown, markdown_label, effective_from, effective_until, whole_price, retailer_store_id]

            array.append(product_list)

    df = pd.DataFrame(array, columns=['Brand', 'sku', 'Available', 'Name', 'Price', 'Unit of Size',
                                      'Size', 'Price', 'Previous Price', 'Discounted', 'Markdown Price',
                                      'Markdown Label', 'Effective From', 'Effective Until', 'Whole Price',
                                      'Store_ID'])
    df.to_csv(output_file)


usage = ''' 
Usage: 
scraper.py [options] <name>

Arguments:
name     output csv file name

Options:
  -h --help           Show this screen.'''


def main():
    args = docopt.docopt(usage)
    list_of_links = \
        create_list_of_links('https://shop.foodland.com/sm/pickup/rsid/50/results?q=sunscreen&page=1&skip=0')
    output = args['<name>']
    export_csv(list_of_links, output)


if __name__ == "__main__":
    main()
