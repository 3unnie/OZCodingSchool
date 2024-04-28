import pymysql;

conn = pymysql.connect(
    host='localhost',  
    user='root',       
    password='1234',  
    db='airbnb',       
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with conn.cursor() as cursor:
    insert_sql = "INSERT INTO Products(productName, price, stockQuantity) VALUES (%s, %s, %s)"
    # cursor.execute(insert_sql,('조먼지의하루',10000,10))
    # conn.commit()

    cursor.execute("SELECT * FROM Products")
    for book in cursor.fetchall():
        print(book)

    update_sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    # cursor.execute(update_sql,(3,13))
    # conn.commit()

    select_sql = "SELECT customerID, SUM(totalAmount) AS totalAmount FROM Orders GROUP BY customerID"
    cursor.execute(select_sql)
    data = cursor.fetchall()
    print(data)

cursor.close()