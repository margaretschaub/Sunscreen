''' Sunscreen
Usage:
docopt.py scrape <brand>
docopt.py create <folder>
docopt.py name <name>
docopt.py merge products
docopt.py test reef safe
docopt.py string matching

Arguments:
    brand       brand name
    name     output csv file
    folder      directory name

Options:

  -l, --all      List all.
  -q, --quit     exit.
  --version      Version 3.6.1
  -h --help      Show this screen.
  --version      Show version.

    '''

from docopt import docopt


def main():
    args = docopt(__doc__, version='0.1')
    name = args['<name>']
    brand = args['<brand>']

    if args['scrape']:
        if brand.lower() == 'sunbum':
            print("1")



if __name__=='__main__':
    main()
