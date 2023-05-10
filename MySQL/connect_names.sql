SELECT DISTINCT 
product_matches.id,
foodland_inventory.brand,
foodland_inventory.product_name AS foodland_name,
product_matches.product_name AS matched_name,
products.item_name As product_master_name,
products.reef_safe_determination
FROM foodland_inventory
	LEFT JOIN product_matches
		ON
		product_matches.foodland_name = foodland_inventory.product_name
	INNER JOIN products
		ON product_matches.product_name = products.item_name
ORDER BY id;



