INSERT IGNORE INTO product_matches (brand, foodland_name, product_name) 
SELECT
foodland_inventory.brand, product_name, item_name FROM foodland_inventory
CROSS JOIN products
WHERE foodland_inventory.product_name = products.item_name;

