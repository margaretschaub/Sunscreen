import pandas as pd

non_reef_safe_ingredients = ['oxybenzone', 'octinoxate', 'octocrylene', 'avobenzone', 'benzophenone',
                           'octisalate', 'homosalate', 'ethylhexyl salicylate']
reef_safe_mineral_ingredients = ['titanium dioxide','zinc oxide']
reef_safe_ingredients = ['non-nano zinc oxide']


def reef_safe_test(csv_path):
    temp = []
    csv_title = pd.read_csv(csv_path)

    for item in csv_title['Active Ingredients']:
        try:
            not_reef_safe = any(ele in item.lower() for ele in non_reef_safe_ingredients)
            mineral = any(ele in item.lower() for ele in reef_safe_mineral_ingredients)
            reef_safe = any(ele in item.lower() for ele in reef_safe_ingredients)
        except AttributeError:
            temp.append('')
            continue

        if not_reef_safe:
            temp.append('0')
        elif reef_safe:
            temp.append('1')
        elif mineral:
            temp.append('2')
        else:
            temp.append('')

    csv_title['Reef Safe Determination'] = temp
    csv_title.to_csv(r'/Users/margaretschaub/Desktop/reef_safe_determination.csv')
    print("CSV exported")


reef_safe_test(r'/Users/margaretschaub/Desktop/lhh.csv')

