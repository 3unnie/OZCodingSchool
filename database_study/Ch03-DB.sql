USE dbstudy;
-- (DDL) 데이터 및 테이블 생성
CREATE TABLE users (
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT
);
-- 데이터 생성 기본적인 INSERT문
INSERT INTO users (user_name, email, age) 
VALUES ('조먼지','MUNJI@NAVER.COM',1);

-- 다수 레코드 한번에 추가
INSERT INTO users (user_name, email, age) 
VALUES 	('조하루','DAY@NAVER.COM',0),
		('조으니','EUNNIE@NAVER.COM',30),
        ('김뚜비','DDUP@NAVER.COM',32);
        
-- 중복된 레코드를 추가하지않고 에러를 방지
INSERT IGNORE INTO users (user_name, email, age)
VALUES ('박철수','CHULSOO@NAVER.COM',5);

-- SET 사용하여 추가
INSERT INTO users 
SET user_name='신짱구', 
	email='JJANG@NAVER.COM', 
    age= 5 ;

-- 데이터 조회 SELECT 문
SELECT * FROM users;
SELECT * FROM users LIMIT 3, 2; -- 갯수제한 3부터 2개
-- 특정 컬럼 만 조회
SELECT user_name, age FROM users;

-- 중복값 삭제 후 조회
SELECT DISTINCT user_name, age FROM users;

-- 데이터 정렬 (DESC:내림차순 / ASC:오름차순)
SELECT * FROM users ORDER BY age DESC; 

-- 일시적 추가 컬럼 만들어 조회
SELECT user_name, age, age * 100 AS age100 FROM users;

-- 조건문 WHERE
SELECT * FROM users WHERE age=5;
SELECT * FROM users WHERE age=1 AND user_name="조먼지";
SELECT * FROM users WHERE age=0 or user_name="조먼지";
SELECT * FROM users WHERE NOT age=32; 
SELECT * FROM users WHERE age BETWEEN 10 AND 35;

-- 조회결과 GROUPING
SELECT age, COUNT(*) AS user_count FROM users GROUP BY age;

-- 특정 조건에 따라 값 변환
SELECT 	user_name, 
		age,
        CASE WHEN age >= 19 THEN '성인' ELSE '미성년자' END AS age_description
FROM users;

-- 순위부여
SELECT  user_name,
		age,
        ROW_NUMBER() OVER (ORDER BY age DESC) AS Urank
FROM users;

-- 데이터 업데이트 UPDATE문
UPDATE users SET user_name = '김요뚭' WHERE user_id =4 LIMIT 5;

-- CASE 문 사용 업데이트
UPDATE users SET user_name = CASE WHEN age >= 60 THEN '노인' ELSE '청년' END;

-- subquery
UPDATE users SET age = age+1 WHERE user_id IN (SELECT user_id FROM users WHERE user_id = 5 or user_id = 6);

-- regexp 정규 표현식을 사용하여 업데이트
UPDATE users SET email = CONCAT(email, '_new') WHERE email REGEXP '@example\.com$';

-- 데이터 제거 DELETE문
DELETE FROM users WHERE age = 5 LIMIT 1;

