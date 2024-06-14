DROP TABLE Products

USE vegetables_and_fruits_db

CREATE TABLE Products
(
	Name NVARCHAR(30) NOT NULL,
	Type NVARCHAR(30) NOT NULL,
	Color NVARCHAR(30) NOT NULL,
	Calories int NOT NULL,
	ShortDescribe text
)

INSERT INTO Products (Name, Type, Color, Calories, ShortDescribe)
VALUES
	('Orange', 'Fruit', 'Orange', 47, 'Cirtus fruit.'),
	('Cucumber', 'Vegetable', 'Green', 18, 'The most popular vegetable.'),
	('Beetroot', 'Vegeable', 'Deep red', 43, 'One of an ingredient for borsch.')


SELECT * FROM Products