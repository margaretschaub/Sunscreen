# Scrapers:

## Scrapers for brand websites:

sun_bum.py generates csv file for Sunbum products

lhh.py generates csv file for Little Hands Hawaii products

hawaiian_tropic.py generates csv file for Hawaiian Tropic products

alba_botanical.py generates csv file for Alba Botanicals products

Run from the command line for each brand:

```
Usage: 
sun_bum.py [options] <name>

Arguments:
name     output csv file name

Options:
  -h --help           Show this screen.
  ```

After running each brand scraper, move CSV files into one directory.
Example of command line argument:
mkdir products_csv && mv alba.csv ht.csv lhh.csv sunbum.csv $_ 

## Scrapers for foodland inventory:

store_info.py generates csv file of store details for each csv location

scraper.py generates csv file of foodland inventory

```
Usage: 
scraper.py [options] <name>

Arguments:
name     output csv file name

Options:
  -h --help           Show this screen.
