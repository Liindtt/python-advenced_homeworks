SELECT * FROM Products
WHERE Type = 'Vegetable' AND Calories < 30;

SELECT * FROM Products
WHERE Type = 'Fruit' AND Calories BETWEEN 40 AND 60;

SELECT * FROM Products
WHERE Type = 'Vegetable' AND Name LIKE '%cucumber%';

SELECT * FROM Products
WHERE ShortDescribe LIKE '%ingredient%';

SELECT * FROM Products
WHERE Color IN ('Green', 'Red');