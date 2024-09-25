SELECT * FROM Products

SELECT * FROM Products
WHERE Type = 'Vegetable' AND Calories < 40

SELECT * FROM Products
WHERE Type = 'Fruit' AND Calories >= 30 AND Calories <= 50

SELECT * FROM Products
WHERE Type = 'Vegetable' AND Name LIKE '%cumber%'

SELECT * FROM Products
WHERE ShortDescribe LIKE '%ingredient%'

SELECT * FROM Products
WHERE Color = 'Green' OR Color = 'Orange'