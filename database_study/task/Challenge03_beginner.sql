-- [beginner]


-- 생성 create

-- (1) customers 테이블에 새 고객을 추가하세요.
INSERT INTO customers(customerNumber,customerName,contactLastName,contactFirstName,phone,addressLine1,addressLine2,city,state,postalCode,country,salesRepEmployeeNumber,creditLimit) VALUES
(1,'조먼지','먼지','조','01012345678','101동101호 고양이아파트','냥냥동','냥냥구','냥냥시','12345','대한민국',1,'20000.00');

-- 2) products 테이블에 새 제품을 추가하세요.
INSERT INTO products(productCode,productName,productLine,productScale,productVendor,productDescription,quantityInStock,buyPrice,MSRP) VALUES
('C01','닭고기츄르','식품','5','냥냥주식회사','천연닭고기100%',99,'4000.00','3000.00');

-- (4) offices 테이블에 새 사무실을 추가하세요.
INSERT INTO offices(officeCode,city,phone,addressLine1,addressLine2,state,country,postalCode,territory) VALUES
('1','냥냥시','1231234','103호','냥빌딩','냥냥구','대한민국','98765','없음');

-- (3) employees 테이블에 새 직원을 추가하세요.
INSERT INTO employees(employeeNumber,lastName,firstName,extension,email,officeCode,reportsTo,jobTitle) VALUES
(1,'하루','조','해당없음','DAY@cat.com','1',NULL,'CEO');

-- (5) orders 테이블에 새 주문을 추가하세요.
INSERT INTO orders(orderNumber,orderDate,requiredDate,shippedDate,status,comments,customerNumber) VALUES
(1,'2024-04-18','2024-04-16','2024-04-15','빠른배송','문앞에놔주세요',1);

-- (6) orderdetails테이블에 주문 상세 정보를 추가하세요.
INSERT INTO orderdetails(orderNumber,productCode,quantityOrdered,priceEach,orderLineNumber) VALUES
(1,'C01',10,'4000.00',1);

-- (7) payments 테이블에 지불 정보를 추가하세요.
INSERT INTO payments(customerNumber,checkNumber,paymentDate,amount) VALUES
(1,'MJ1','2024-04-18','40000.00');

-- (8) productlines 테이블에 제품 라인을 추가하세요.
INSERT INTO productlines(productLine,textDescription,htmlDescription,image) VALUES
('식품','냠냠쩝쩝',NULL,NULL);
INSERT INTO productlines(productLine,textDescription,htmlDescription,image) VALUES
('생활','필요해',NULL,NULL);

-- (9) customers 테이블에 다른 지역의 고객을 추가하세요.
INSERT INTO customers(customerNumber,customerName,contactLastName,contactFirstName,phone,addressLine1,addressLine2,city,state,postalCode,country,salesRepEmployeeNumber,creditLimit) VALUES
(2,'조으니','으니','조','01098765432','101동101호 사람아파트','사람동','사람구','사람시','98765','대한민국',1,'100000.00');

-- (10) products 테이블에 다른 카테고리의 제품을 추가하세요.
INSERT INTO products(productCode,productName,productLine,productScale,productVendor,productDescription,quantityInStock,buyPrice,MSRP) VALUES
('H01','물티슈','생활','10','사람주식회사','면100%',99,'2000.00','1000.00');

-- 읽기 read

-- (1) customers 테이블에서 모든 고객 정보를 조회하세요.
SELECT * FROM customers;

-- (2) products 테이블에서 모든 제품 목록을 조회하세요.
SELECT * FROM products;

-- (3) employees 테이블에서 모든 직원의 이름과 직급을 조회하세요.
SELECT lastName, firstName, jobTitle FROM employees;

-- (4) offices 테이블에서 모든 사무실의 위치를 조회하세요.
SELECT addressLine1,addressLine2,state,city,country FROM offices;

-- (5) orders 테이블에서 최근 10개의 주문을 조회하세요.
SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10; 

-- (6) orderdetails 테이블에서 특정 주문의 모든 상세 정보를 조회하세요.
SELECT * FROM orderdetails WHERE orderNumber = 1;

-- (7) payments 테이블에서 특정 고객의 모든 지불 정보를 조회하세요.
SELECT * FROM payments WHERE customerNumber=1;

-- (8) productlines 테이블에서 각 제품 라인의 설명을 조회하세요.
SELECT productLine, textDescription FROM productlines;

-- (9) customers 테이블에서 특정 지역의 고객을 조회하세요.
SELECT * FROM customers WHERE city = '냥냥구';

-- (10) products 테이블에서 특정 가격 범위의 제품을 조회하세요.
SELECT * FROM products WHERE buyPrice > 3000 and buyPrice < 5000;

-- 갱신 update

-- (1) customers 테이블에서 특정 고객의 주소를 갱신하세요.
UPDATE customers SET addressLine1 = '어딘가' WHERE customerNumber=2;

-- (2) products 테이블에서 특정 제품의 가격을 갱신하세요.
UPDATE products SET buyPrice=2000 WHERE productCode ='C01';

-- (3) employees 테이블에서 특정 직원의 직급을 갱신하세요.
UPDATE employees SET jobTitle='대표' WHERE employeeNumber=1;

-- (4) offices 테이블에서 특정 사무실의 전화번호를 갱신하세요.
UPDATE offices SET phone='0000000' WHERE officeCode = '1';

-- (5) orders 테이블에서 특정 주문의 상태를 갱신하세요.
UPDATE orders SET status='반품' WHERE orderNumber=1;

-- (6) orderdetails 테이블에서 특정 주문 상세의 수량을 갱신하세요.
UPDATE orderdetails SET quantityOrdered=5 WHERE orderNumber=1;

-- (7) payments 테이블에서 특정 지불의 금액을 갱신하세요.
UPDATE payments SET amount = 20000.00 WHERE customerNumber=1;

-- (8) productlines 테이블에서 특정 제품 라인의 설명을 갱신하세요.
UPDATE productlines SET textDescription = '맛도리재품들' WHERE productLine='식품';

-- (9) customers 테이블에서 특정 고객의 이메일을 갱신하세요.
UPDATE customers SET email = 'MUNJI@CAT.com' WHERE customerNumber=1;

-- (10) products 테이블에서 여러 제품의 가격을 한 번에 갱신하세요.
UPDATE products SET buyPrice = buyPrice * 2 WHERE productLine ='생활';

-- 삭제 delete

-- (1) customers 테이블에서 특정 고객을 삭제하세요.
DELETE FROM customers WHERE customerNumber = 1; 

-- (2) products테이블에서 특정 제품을 삭제하세요.
DELETE FROM products WHERE productCode ='C01';

-- (3) employees 테이블에서 특정 직원을 삭제하세요.
DELETE FROM employees WHERE  employeeNumber=1;

-- (4) offices 테이블에서 특정 사무실을 삭제하세요.
DELETE FROM offices WHERE officeCode='1';

-- (5) orders 테이블에서 특정 주문을 삭제하세요.
DELETE FROM  orders WHERE orderNumber=1;

-- (6) orderdetails 테이블에서 특정 주문 상세를 삭제하세요.
DELETE FROM orderdetails WHERE orderNumber=1;

-- (7) payments 테이블에서 특정 지불 내역을 삭제하세요.
DELETE FROM payments WHERE customerNumber=1;

-- (8) productlines 테이블에서 특정 제품 라인을 삭제하세요.
DELETE FROM productlines WHERE productLine = '생활'; 

-- (9) customers 테이블에서 특정 지역의 모든 고객을 삭제하세요.
DELETE FROM customers WHERE city='사람구';

-- (10) products 테이블에서 특정 카테고리의 모든 제품을 삭제하세요.
DELETE FROM products WHERE productLine='식품';