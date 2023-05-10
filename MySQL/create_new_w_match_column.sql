    CREATE TABLE IF NOT EXISTS foodland_inventory_new (id INT AUTO_INCREMENT PRIMARY KEY, 
                        brand varchar(255), 
                        sku varchar(255), 
                        available tinyint, 
                        product_name varchar(255),
                        match_id INT,
                        price varchar(255), 
                        unit_of_size varchar(255), 
                        size DECIMAL(5,2), 
                        price_per_size varchar(255), 
                        previous_price varchar(255), 
                        discounted tinyint,
                        markdown_price DECIMAL(5,2), 
                        markdown_label varchar(255), 
                        effective_from datetime, 
                        effective_until datetime, 
                        whole_price DECIMAL(5,2), 
                        retailer_store_id INT,
                        FOREIGN KEY (retailer_store_id) REFERENCES retailer_stores(retailer_store_id),
                        UNIQUE(sku, retailer_store_id));
                        
CREATE TABLE IF NOT EXISTS products_new 
(id INT AUTO_INCREMENT PRIMARY KEY,
url varchar(600),
item_name varchar(150),
match_id INT,
ingredients LONGTEXT, 
reef_safe_determination INT,
brand varchar(100),
UNIQUE (item_name, url),
FOREIGN KEY(reef_safe_determination) REFERENCES reef_key(key_entry)
    ); 
    
