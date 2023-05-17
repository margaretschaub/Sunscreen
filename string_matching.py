from fuzzywuzzy import fuzz, process
import pandas as pd
from scrapers.import_export_file import arg_1, arg_2, arg_3


def read_csv(file_name):
    csv = pd.read_csv(file_name)
    return csv


def match_names(file_1, file_2, table, output_file):
    mat1 = []
    mat2 = []
    p = []
    threshold = 100

    # process.extractOne returns only one output which contains the string with the highest matching score
    for i in file_1:
        mat1.append(process.extractOne(
            i, file_2, scorer=fuzz.token_set_ratio))

    table['matches'] = mat1

    for j in table['matches']:
        if j[1] >= threshold:
            p.append(j[0])
        mat2.append(",".join(p))
        p = []
    table['matches'] = mat2
    table.to_csv(output_file)


def main():
    product_file = arg_1()
    grocery_file = arg_2()

    foodland_df = read_csv(grocery_file)
    product_df = read_csv(product_file)

    foodland_name_list = foodland_df['foodland_name'].tolist()  # file 1
    product_name_list = product_df['item_name'].tolist()  # file 2

    output_file = arg_3()
    match_names(foodland_name_list, product_name_list, foodland_df, output_file)


if __name__ == "__main__":
    main()
