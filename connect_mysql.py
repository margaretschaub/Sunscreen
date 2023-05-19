import pandas as pd
import mysql.connector as msql
from mysql.connector import Error
import docopt


usage = ''' 
Usage: 
connect_mysql.py [options] <password> <table> <input>

Arguments:
password
name     output csv file name
table    table name to load into: store, inventory, product, matches
input    input csv file

Options:
  -h --help           Show this screen.
  store               load into retailer_stores table
  inventory           load into foodland_inventory table
  product             load into products table
  matches             load into product_matches table
  '''
args = docopt.docopt(usage)


def sql_commit(dataframe, sql_statement):
    try:
        conn = msql.connect(host='localhost', user='root',
                            password=args['<password>'])
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("USE sunscreen;")
            for i, row in dataframe.iterrows():
                sql = sql_statement
                cursor.execute(sql, tuple(row))
                print("Record inserted")
                conn.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)


def clean_df(file_name):
    df_object = pd.read_csv(file_name, delimiter=',')
    df_object = df_object.drop(columns=['Unnamed: 0'])
    return df_object


def load_foodland_info():
    sql = '''INSERT IGNORE INTO retailer_stores (retailer_store_id, store_name,
    address_line1,address_line2, state, post_code, city, coordinate)
    VALUES(%s, %s, %s, %s, %s ,%s, %s, %s);'''
    foodland_csv = args['<input>']
    foodland_info = clean_df(foodland_csv)
    sql_commit(foodland_info, sql)


def load_products():
    sql = '''INSERT IGNORE INTO products (url, item_name,
    ingredients, reef_safe_determination) VALUES (%s,%s,%s,%s)'''
    products_csv = args['<input>']
    products_df = clean_df(products_csv)
    products_df = products_df.astype(object).where(pd.notnull(products_df), None).tail(-1)
    sql_commit(products_df, sql)


def load_product_matches():
    sql = '''INSERT IGNORE INTO product_matches (brand,foodland_name, product_name)
    VALUES (%s,%s,%s)'''
    product_match_csv = args['<input>']
    product_match_df = clean_df(product_match_csv)
    product_match_df = product_match_df.astype(object).where(pd.notnull(product_match_df), None)
    sql_commit(product_match_df, sql)


def load_inventory():
    sql = '''INSERT IGNORE INTO foodland_inventory (brand, sku,
                available,
                product_name,
                price,
                unit_of_size,
                size,
                price_per_size,
                previous_price,
                discounted,
                markdown_price,
                markdown_label,
                effective_from,
                effective_until,
                whole_price,
                retailer_store_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    inventory_csv = args['<input>']
    inventory_df = clean_df(inventory_csv)
    inventory_df = inventory_df.astype(object).where(pd.notnull(inventory_df), None)
    sql_commit(inventory_df, sql)


def main():
    args = docopt.docopt(usage)
    if args['<table>'].lower() == 'store':
        load_foodland_info()
    elif args['<table>'].lower() == 'inventory':
        load_inventory()
    elif args['<table>'].lower() == 'product':
        load_products()
    elif args['<table>'].lower() == 'matches':
        load_product_matches()
    else:
        print("Incorrect argument for table to load  into. Try ---help")


if __name__ == "__main__":
    main()
