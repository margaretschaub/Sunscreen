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

Note:
Some of the product information I added by hand. For example, Sol Remedies only has one product,
so it was more productive to write this information by hand than create a unique scraper. The CSV with additional product information beyond what was obtained by the scrapers is
available in the CSVs folder. I recommend using reef_safe_determination.csv as a master product list.

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
