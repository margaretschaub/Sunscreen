CREATE DATABASE IF NOT EXISTS sunscreen;

USE sunscreen;

CREATE TABLE IF NOT EXISTS reef_key
	(id INT AUTO_INCREMENT PRIMARY KEY,
    key_entry INT,
    explanation MEDIUMTEXT,
    UNIQUE (key_entry)
    );


CREATE TABLE IF NOT EXISTS retailer_stores
	(id INT AUTO_INCREMENT PRIMARY KEY,
    retailer_store_id INT NOT NULL,
    store_name varchar(255), 
    address_line1 varchar(255), 
    address_line2 varchar(255), 
    state varchar(255), 
    post_code INT, 
    city varchar(255), 
	coordinate VARCHAR(255),
    UNIQUE (retailer_store_id));
    
    
CREATE TABLE IF NOT EXISTS foodland_inventory (id INT AUTO_INCREMENT PRIMARY KEY, 
		brand varchar(255), 
		sku varchar(255), 
		available tinyint, 
		product_name varchar(255),
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
                        
CREATE TABLE IF NOT EXISTS products 
	(id INT AUTO_INCREMENT PRIMARY KEY,
	url varchar(600),
	item_name varchar(150),
	ingredients LONGTEXT, 
	reef_safe_determination INT,
	brand varchar(100),
	UNIQUE (item_name, url),
	FOREIGN KEY(reef_safe_determination) REFERENCES reef_key(key_entry)
		);                        


CREATE TABLE IF NOT EXISTS product_matches 
	(id INT AUTO_INCREMENT PRIMARY KEY, 
	brand varchar(250),
	foodland_name varchar(250),
	product_name varchar(250),
	UNIQUE (foodland_name, product_name));


CREATE TABLE IF NOT EXISTS corrections 
	(id INT AUTO_INCREMENT PRIMARY KEY,
	product_id INT,
	corrected_unit varchar(255),
	corrected_size DECIMAL(5,2),
	FOREIGN KEY (product_id) REFERENCES product_matches (id),
	UNIQUE (product_id));

INSERT INTO reef_key (key_entry, explanation) 
VALUES   (0, "Banned in Hawaii. Includes oxybenzone and octinoxate, went into effect on January 1, 2021");
INSERT INTO reef_key (key_entry, explanation) 
VALUES   (1, "Not reef safe. Contains chemicals proposed to be banned in Hawaii like Octocrylene and Avobenzone");
INSERT INTO reef_key (key_entry, explanation) 
VALUES   (2, "Mineral. Mineral sunscreen is healthier for reef than chemicals, but effects of titanium dioxide are unknown. May contain nano-particles");
INSERT INTO reef_key (key_entry, explanation) 
VALUES   (3, "Reef safe. Only active ingredient is non-nano zinc oxide."); 