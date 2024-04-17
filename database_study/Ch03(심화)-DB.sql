USE dbstudy;
CREATE TABLE users (
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT
);
CREATE TABLE orders (
	order_id INT PRIMARY KEY AUTO_INCREMENT,
	user_id INT NOT NULL,
    product_name VARCHAR(255),
    quantitiy INT,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

-- 파이썬으로 데이터 렌덤 생성
SELECT * From users;
SELECT * FROM orders order by user_id;