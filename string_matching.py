from fuzzywuzzy import fuzz, process
import pandas as pd
from import_export_file import output_file_path


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


def input_grocery_file():
    while True:
        try:
            grocery_file = input("Grocery inventory csv hard coded path: ")
            return grocery_file
        except FileNotFoundError:
            print("No such file or directory. Please try again.")


def input_product_file():
    while True:
        try:
            product_file = input("Product csv hard coded path: ")
            return product_file
        except FileNotFoundError:
            print("No such file or directory. Please try again.")


def main():
    grocery_file = input_grocery_file()
    product_file = input_product_file()

    foodland_df = read_csv(grocery_file)
    product_df = read_csv(product_file)

    foodland_name_list = foodland_df['foodland_name'].tolist()  # file 1
    product_name_list = product_df['item_name'].tolist()  # file 2

    output_file = output_file_path()
    match_names(foodland_name_list, product_name_list, foodland_df, output_file)


if __name__ == "__main__":
    main()
