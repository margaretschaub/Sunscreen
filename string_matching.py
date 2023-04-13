from fuzzywuzzy import fuzz, process
import pandas as pd

foodland = pd.read_csv(r'/Users/margaretschaub/Desktop/foodland_needs_match.csv')
product = pd.read_csv(r'/Users/margaretschaub/Desktop/master_products.csv')

foodland_name = foodland['foodland_name'].tolist()
product_name = product['item_name'].tolist()

mat1 = []
mat2 = []
p = []
threshold = 100

##process.extractOne returns only one output which contains the string with the highest matching score
for i in foodland_name:
    mat1.append(process.extractOne(
        i, product_name, scorer=fuzz.token_set_ratio))

foodland['matches'] = mat1

for j in foodland['matches']:
    if j[1] >= threshold:
        p.append(j[0])
    mat2.append(",".join(p))
    p = []
foodland['matches'] = mat2
foodland.to_csv(r'/Users/margaretschaub/Desktop/foodlandsunscreen_matches.csv')
