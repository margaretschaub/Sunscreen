INSERT INTO foodland_inventory_new
SELECT 
foodland_inventory.id,
foodland_inventory.brand,
foodland_inventory.sku,
foodland_inventory.available,
foodland_inventory.product_name,
product_matches.id,
foodland_inventory.price,
foodland_inventory.unit_of_size,
foodland_inventory.size,
foodland_inventory.price_per_size,
foodland_inventory.previous_price,
foodland_inventory.discounted,
foodland_inventory.markdown_price,
foodland_inventory.markdown_label,
foodland_inventory.effective_from,
foodland_inventory.effective_until,
foodland_inventory.whole_price,
foodland_inventory.retailer_store_id
FROM foodland_inventory
INNER JOIN product_matches
ON foodland_inventory.product_name = product_matches.foodland_name
INNER JOIN products
ON product_matches.product_name = products.item_name;

INSERT IGNORE INTO products_new
SELECT 
products.id,
products.url,
products.item_name,
product_matches.id,
products.ingredients,
products.reef_safe_determination,
products.brand
FROM foodland_inventory
INNER JOIN product_matches
ON foodland_inventory.product_name = product_matches.foodland_name
RIGHT JOIN products
ON product_matches.product_name = products.item_name
ORDER BY products.id;

SELECT * FROM sunscreen.foodland_inventory
WHERE PRICE LIKE '%$%';

UPDATE foodland_inventory_new set price=substr(price,2)
