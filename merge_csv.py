import os
import pandas as pd
import docopt


def merge_csv_files(file_path, output_file_location):
    file_list = os.listdir(file_path)
    absolute_path_list = []
    for file in file_list:
        absolute_path = f'{file_path}/{file}'
        absolute_path_list.append(absolute_path)

    df_append = pd.DataFrame(columns=['URL', 'Item Name', 'Ingredients'])

    li = []
    for file in absolute_path_list:
        df_temp = pd.read_csv(file, index_col=None, encoding="utf-8", header=0)
        li.append(df_temp)
        df_append = pd.concat(li, axis=0, ignore_index=True)
        df_append = df_append.drop(columns=['Unnamed: 0'])

    df_append.to_csv(output_file_location)


usage = ''' 
Usage: 
merge_csv.py [options] <directory> <name>

Arguments:
directory directory with csv files
name     output csv file name

Options:
  -h --help           Show this screen.'''


def main():
    args = docopt.docopt(usage)
    input_path = args['<directory>']
    output_path = args['<name>']
    merge_csv_files(input_path, output_path)


if __name__ == "__main__":
    main()
