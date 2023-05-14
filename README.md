I designed an interactive tool to investigate sunscreens sold in Hawaii. The purpose of this tool is two-fold: 

Inform consumers of the pricing and availability of sunscreens in each of the reef-safety categories at specific stores

Identify the “best buy” for reef-safe sunscreen

Check out more on my website at https://www.macischaub.com/projects/sunscreen-analysis

I chose to start the project investigating Foodland’s inventory since their website offers the ability to shop online and view products available in each store. I used the Beautiful Soup Python library to write a web page scraper. I downloaded a CSV file of the sunscreen inventory at each Foodland location with an online shopping option. I also wrote scrapers for each sunscreen brand’s webpages to download the ingredient information for each product. I then wrote a Python program that scans each word in a product’s ingredients list and assigns a reef safety status score based on the ingredients contained in the product using the following key: 
I created a database using MySQL. I outlined the following tables: store information, inventory data with a foreign key to each store, product list with ingredients and reef-safe status, and a reef safe status key. I cleaned the inventory and product data with Python using the Pandas library and established a cursor connection to load the CSVs into MySQL. 

I then solved the following challenge: matching the name of the product sold at Foodland to the name of the product on its brand website. I did this in order to link each sunscreen sold at Foodland with its reef safety status score. I created an additional table to hold the matched product names. I used a MySQL join to match products with identical names. I wrote a Python program using fuzzy string matching to identify the remaining name pairs. Each name match corresponds to a primary key. I created both new inventory and product tables, each with a new column containing a foreign key corresponding to the primary key of the name match table. With this update, even if the product names differ between the inventory and product details table, the products can be linked with the foreign key. I used MySQL to identify missing data and further clean data. I imported the database tables into Tableau to create the dashboards.

References used for general learning:

https://medium.com/@stella96joshua/how-to-combine-multiple-csv-files-using-python-for-your-analysis-a88017c6ff9e

https://www.geeksforgeeks.org/python-test-if-string-contains-element-from-list/

https://www.geeksforgeeks.org/how-to-do-fuzzy-matching-on-pandas-dataframe-column-using-python/

https://towardsdatascience.com/fuzzywuzzy-fuzzy-string-matching-in-python-beginners-guide-9adc0edf4b35

https://typesense.org/learn/fuzzy-string-matching-python/

https://beautiful-soup-4.readthedocs.io/en/latest/

https://tedboy.github.io/bs4_doc/9_specifying_the_parser.html

https://sparkbyexamples.com/pandas/pandas-apply-function-usage-examples/

https://stackoverflow.com/questions/20906474/import-multiple-csv-files-into-pandas-and-concatenate-into-one-dataframe

https://www.projectpro.io/recipes/connect-mysql-python-and-import-csv-file-into-mysql-and-create-table

