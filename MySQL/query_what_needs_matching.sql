SELECT DISTINCT brand, foodland_name FROM
(SELECT foodland_inventory.brand, foodland_inventory.product_name AS foodland_name,
product_matches.product_name, product_matches.id 
FROM foodland_inventory
LEFT JOIN sunscreen.product_matches
ON foodland_inventory.product_name = product_matches.foodland_name) sub
WHERE id is null
ORDER BY brand
;







