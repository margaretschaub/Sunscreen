''' Sunscreen
Usage:
docopt.py scrape <brand> to <name>
docopt.py create <folder>
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


brand = args['<brand>']
name = args['<name>']
