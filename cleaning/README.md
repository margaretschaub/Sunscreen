# Data Cleaning

## Merge Brand CSVs

use merge_csv.py to merge csv files for brand products into one csv

brand CSVs should be in one directory (see scrapers README)
```Usage: 
merge_csv.py [options] <directory> <name>

Arguments:
directory directory with csv files
name     output csv file name

Options:
  -h --help           Show this screen.
  ```

## Reef Safety Status

reef_safe.py analyzes a reef safety score for each product

this program's input file is the merged csv output from merge_csv.py

```Usage: 
reef_safe.py [options] <input> <name>

Arguments:
input    input csv file
name     output csv file name

Options:
  -h --help           Show this screen.
  ```

## Matching Foodland Products & Brand Products

string_matching.py uses the fuzzywuzzy library for fuzzy string matching between the foodland 
sunscreen inventory list and the sunscreen list from brand websites. 

I used token set ratio so that, for example,
"Sun Bum Mineral Lotion Face SPF 30" from Foodland's website and "Mineral SPF 30 Sunscreen Face Lotion– Sun Bum"
from Sun Bum's website would be matched as the same product. 

```Usage: 
string_matching.py [options] <product> <grocery> <name>

Arguments:
product    product details csv file
grocery     grocery inventory csv file name
name     output csv file name

Options:
  -h --help           Show this screen.
  ```
