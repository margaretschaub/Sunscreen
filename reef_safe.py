import pandas as pd
import docopt

banned_ingredients = ['oxybenzone', 'octinoxate']

non_reef_safe_ingredients = ['octocrylene', 'avobenzone', 'benzophenone', 'octisalate',
                             'homosalate', 'ethylhexyl salicylate']

reef_safe_mineral_ingredients = ['titanium dioxide', 'zinc oxide']

reef_safe_ingredients = ['non-nano zinc oxide', 'non-nano zinc', '(Non-Nano) Zinc Oxide']


def reef_safe_test(input_csv_path, output_csv_path):
    temp = []
    csv_title = pd.read_csv(input_csv_path)

    for item in csv_title['Ingredients']:
        try:
            banned = any(ele in item.lower() for ele in banned_ingredients)
            not_reef_safe = any(ele in item.lower() for ele in non_reef_safe_ingredients)
            mineral = any(ele in item.lower() for ele in reef_safe_mineral_ingredients)
            reef_safe = any(ele in item.lower() for ele in reef_safe_ingredients)
        except AttributeError:
            temp.append('')
            continue

        if not_reef_safe:
            temp.append('1')
        elif reef_safe:
            temp.append('3')
        elif mineral:
            temp.append('2')
        elif banned:
            temp.append('0')
        else:
            temp.append('')

    csv_title['Reef Safe Determination'] = temp

    csv_title.to_csv(output_csv_path, index=False)
    print("CSV exported")


usage = ''' 
Usage: 
reef_safe.py [options] <input> <name>

Arguments:
input    input csv file
name     output csv file name

Options:
  -h --help           Show this screen.'''


def main():
    args = docopt.docopt(usage)
    input_path = args['<input>']
    output_path = args['<name>']
    reef_safe_test(input_path, output_path)


if __name__ == "__main__":
    main()
