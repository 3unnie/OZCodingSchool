# pip install mysql-connector-python faker
import mysql.connector
from faker import Faker
import random

# 1.MYSQL 연결초기 셋팅
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='dbstudy'
)

#2.연결
cursor = db_connection.cursor()
faker = Faker()

#USERS 더미데이터생성
for _ in range(100):
    userName = faker.user_name()
    email = faker.email()
    age = random.randint(1,20)

    sql = "INSERT INTO users (user_name, email,age) VALUES (%s,%s,%s)"
    values = (userName,email,age)

    cursor.execute(sql,values)

#user_id가져오기
cursor.execute("SELECT user_id From users")
valid_user_id = [row[0] for row in cursor.fetchall()]

#ORDERS 더미데이터 생성
for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantitiy = random.randint(1,10)
    
    sql = "INSERT INTO orders (user_id, product_name, quantitiy) VALUES (%s,%s,%s)"
    values = (user_id, product_name, quantitiy)

    cursor.execute(sql,values)


db_connection.commit()
cursor.close()
db_connection.close()