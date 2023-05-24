from fuzzywuzzy import fuzz, process
import pandas as pd
import numpy as np
import docopt


def read_csv(file_name):
    csv = pd.read_csv(file_name)
    return csv


def match_names(file_1, file_2, table):
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
    return table


usage = ''' 
Usage: 
string_matching.py [options] <product> <grocery> <name>

Arguments:
product    product details csv file
grocery     grocery inventory csv file name
name     output csv file name

Options:
  -h --help           Show this screen.'''


def main():
    args = docopt.docopt(usage)
    product_file = args['<product>']
    grocery_file = args['<grocery>']

    foodland_df = read_csv(grocery_file)
    product_df = read_csv(product_file)

    foodland_name_list = foodland_df['Name'].tolist()  # file 1
    product_name_list = product_df['Item Name'].tolist()  # file 2

    fuzz_df = foodland_df[['Brand', 'Name']].copy()

    output_file = args['<name>']
    temp = match_names(foodland_name_list, product_name_list, fuzz_df)
    temp = temp.replace(r'^\s*$', np.nan, regex=True)
    cleaned = temp.dropna(subset=['matches'])
    cleaned.to_csv(output_file)


if __name__ == "__main__":
    main()
