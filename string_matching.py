from fuzzywuzzy import fuzz, process
import pandas as pd

foodland = pd.read_csv(r'/Users/margaretschaub/Desktop/foodlandsunscreen.csv')
sunbum = pd.read_csv(r'/Users/margaretschaub/Desktop/sunbum2.csv')

product_name_foodland =foodland['Name'].tolist()
product_name_sunbum = sunbum['Item Name'].tolist()

mat1 = []
mat2 = []
p = []
threshold = 80

##process.extractOne returns only one output which contains the string with the highest matching score
for i in product_name_foodland:
    mat1.append(process.extractOne(
        i, product_name_sunbum, scorer=fuzz.token_set_ratio))

foodland['matches'] = mat1

for j in foodland['matches']:
    if j[1] >= threshold:
        p.append(j[0])
    mat2.append(",".join(p))
    p = []
foodland['matches'] = mat2
foodland.to_csv(r'/Users/margaretschaub/Desktop/foodlandsunscreen_matches.csv')
