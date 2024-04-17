-- 데이터베이스 생성
-- CREATE DATABASE DBstudy;
-- 데이터 베이스 목록 조회
-- SHOW DATABASES;
-- 데이터베이스 사용
-- USE DBstudy;
-- 데이터베이스 삭제
-- DROP DATABASE IF EXISTS mydatabase;

-- (DDL) 데이터 베이스 정의 언어
-- (DML) 데이터 베이스 처리 언어
-- (DCL) 데이터 베이스 사용자의 권한을 관리고 데이터 접근을 제어 하는 언어
-- (TCL) 데이터 베이스 내의 트랜잭션을 관리하는 언어

-- USE mysql;
-- SELECT * FROM USER;

-- 유저 생성
-- CREATE USER 'eunnie'@'localhost' IDENTIFIED BY 'eunnie_password';
-- 사용자 비밀번호 변경
-- SET PASSWORD FOR 'eunnie'@'%' = '신규비밀번호';
-- 권한 부여
-- GRANT ALL PRIVILEGES ON *.* TO 'eunnie'@'localhost'; #부여
-- FLUSH PRIVILEGES; #변경된 권한 적용
-- SHOW GRANTS FOR 'eunnie'@'localhost'; #부여된 권한 확인
-- SHOW GRANTS; #현재 로그인한 유저의 권한 확인
-- 사용자 삭제
-- DROP USER 'eunnie'@'localhost';

-- ------------------------------------
-- CREATE TABLE users (
-- 		id 			INT AUTO_INCREMENT PRIMARY KEY,
--     	username 	VARCHAR(50) NOT NULL,
--     	email		VARCHAR(100) UNIQUE,
--     	is_business	VARCHAR(10) DEFAULT False,
--     	age 		INT CHECK (age >= 10)
-- );

-- CREATE TABLE users (
-- 	user_id INT PRIMARY KEY,
--     name 	VARCHAR(100),
--     age 	INT
-- );

-- INSERT INTO users (user_id, name, age)
-- VALUES 	(1, '조먼지', 1),
-- 		(2, '조하루', 0),
-- 		(3, '조으니', 30),
-- 		(4, '김뚜비', 32);

-- SELECT * FROM DBstudy.users;

-- CREATE TABLE orders(
-- 	order_id	INT PRIMARY KEY,
--     user_id		INT,
--     order_date 	DATETIME
-- );

-- INSERT INTO orders (order_id, user_id, order_date)
-- VALUES (101, 1, '2023-06-05'),(102, 2, '2024-03-14'),(103, 3, '2024-04-14'),(104, 4, '2023-07-14');

-- SELECT * FROM DBstudy.orders;
