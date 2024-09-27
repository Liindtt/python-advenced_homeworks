-- Створення таблиці продуктів (products)
CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    type VARCHAR(50),
    color VARCHAR(50),
    calories INT,
    short_description TEXT
);

-- Створення таблиці категорій (categories)
CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(50) NOT NULL
);

-- Створення таблиці-зв'язку між продуктами і категоріями (product_category)
CREATE TABLE product_category (
    product_id INT,
    category_id INT,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);


-- Вставка продуктів
INSERT INTO products (name, type, color, calories, short_description)
VALUES
('Cucumber', 'Vegetable', 'Green', 18, 'The most popular vegetable.'),
('Orange', 'Fruit', 'Orange', 47, 'Citrus fruit.'),
('Beetroot', 'Vegetable', 'Deep red', 43, 'One of an ingredient for borscht.');

-- Вставка категорій
INSERT INTO categories (category_name)
VALUES
('Vegetables'),
('Fruits');

-- Зв'язування продуктів з категоріями
INSERT INTO product_category (product_id, category_id)
VALUES
(1, 1), -- Cucumber -> Vegetables
(2, 2), -- Orange -> Fruits
(3, 1); -- Beetroot -> Vegetables

DELETE FROM products WHERE id = 1;

