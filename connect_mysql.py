import pandas as pd
import mysql.connector as msql
from mysql.connector import Error


empdata = pd.read_csv(r'/Users/margaretschaub/Desktop/foodland_sunscreen2.csv', delimiter=',')
empdata = empdata.drop(columns=['Unnamed: 0'])
foodland_info = pd.read_csv(r'/Users/margaretschaub/Desktop/foodland_store_details.csv', delimiter=',')
foodland_info = foodland_info.drop(columns=['Unnamed: 0'])

df = empdata.astype(object).where(pd.notnull(empdata), None)

products = pd.read_csv(r'/Users/margaretschaub/Desktop/reef_safe_determination.csv', delimiter=',')
products = products.drop(columns=['Unnamed: 0'])
products_df = products.astype(object).where(pd.notnull(products), None).tail(-1)

product_match = pd.read_csv(r'/Users/margaretschaub/Desktop/foodlandsunscreen_matches.csv', delimiter=',')
product_match_df = product_match.astype(object).where(pd.notnull(product_match), None)
product_match_df = product_match_df.drop(columns=['Unnamed: 0'])

# try:
#     conn = msql.connect(host='localhost', user='root',
#                         password='maceee23')  # give ur username, password
#     if conn.is_connected():
#         cursor = conn.cursor()
#         cursor.execute("USE sunscreen;")
#         for i, row in foodland_info.iterrows():
#             # here %S means string values
#             sql = '''INSERT INTO retailer_stores (retailer_store_id, store_name,
#             address_line1,address_line2, state, post_code, city, coordinate)
#             VALUES(%s, %s, %s, %s, %s ,%s, %s, %s);'''
#             cursor.execute(sql, tuple(row))
#             print("Record inserted")
#             # the connection is not auto committed by default, so we must commit to save our changes
#             conn.commit()
# except Error as e:
#     print("Error while connecting to MySQL", e)

# try:
#     conn = msql.connect(host='localhost', user='root',
#                         password='maceee23')  # give ur username, password
#     if conn.is_connected():
#         cursor = conn.cursor()
#         cursor.execute("USE sunscreen;")
#         for i, row in df.iterrows():
#             # here %S means string values
#             sql = '''INSERT INTO sunscreen.foodland_inventory (brand, sku,
#                         available,
#                         product_name,
#                         price,
#                         unit_of_size,
#                         size,
#                         price_per_size,
#                         previous_price,
#                         discounted,
#                         markdown_price,
#                         markdown_label,
#                         effective_from,
#                         effective_until,
#                         whole_price,
#                         retailer_store_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
#             cursor.execute(sql, tuple(row))
#             print("Record inserted")
#             # the connection is not auto committed by default, so we must commit to save our changes
#             conn.commit()
# except Error as e:
#     print("Error while connecting to MySQL", e)
                        
# try:
#     conn = msql.connect(host='localhost', user='root',
#                         password='maceee23')  # give ur username, password
#     if conn.is_connected():
#         cursor = conn.cursor()
#         cursor.execute("USE sunscreen;")
#         for i, row in products_df.iterrows():
#             # here %S means string values
#             sql = '''INSERT INTO sunscreen.products (url, item_name,
#             ingredients, reef_safe_determination) VALUES (%s,%s,%s,%s)'''
#             cursor.execute(sql, tuple(row))
#             print("Record inserted")
#             # the connection is not auto committed by default, so we must commit to save our changes
#             conn.commit()
# except Error as e:
#     print("Error while connecting to MySQL", e)

try:
    conn = msql.connect(host='localhost', user='root',
                        password='maceee23')  # give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("USE sunscreen;")
        for i, row in product_match_df.iterrows():
            # here %S means string values
            sql = '''INSERT IGNORE INTO sunscreen.product_matches (brand,foodland_name, product_name) 
            VALUES (%s,%s,%s)'''
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)