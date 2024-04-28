import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='dbstudy',
    cursorclass=pymysql.cursors.DictCursor,  #딕셔너리 형으로 저장됨 없으면 튜플형으로 가져옴 key값 이없다는걸 유의
    charset='utf8mb4',
)
# cursorclass
#    1. Default Cursor (`pymysql.cursors.Cursor`): 기본 커서 클래스로, 결과를 튜플 형식으로 반환합니다. 각 행은 값들의 튜플로 나타나며, 열 이름 정보는 포함하지 않습니다.
#    2. DictCursor (`pymysql.cursors.DictCursor`): 이 커서 클래스는 결과를 딕셔너리 형식으로 반환합니다. 각 행은 열 이름을 키로 하고 해당 데이터를 값으로 하는 딕셔너리로 나타납니다. 이는 결과를 처리할 때 열 이름으로 데이터에 접근할 수 있게 해줘 편리합니다.
#    3. SSCursor (`pymysql.cursors.SSCursor`): 서버 사이드 커서로, 큰 결과 집합을 처리할 때 유용합니다. 이 커서는 모든 결과를 한 번에 메모리에 로드하지 않고, 필요할 때마다 서버에서 행을 가져옵니다.
#    4. SSDictCursor (`pymysql.cursors.SSDictCursor`): 서버 사이드 딕셔너리 커서로, **`SSCursor`**의 기능에 딕셔너리 형식의 결과 반환을 추가합니다. 큰 데이터 집합에서 열 이름으로 데이터에 접근해야 할 때 유용합니다.
#    5. NamedTupleCursor (`pymysql.cursors.NamedTupleCursor`): 이 커서는 결과를 명명된 튜플(namedtuple) 형식으로 반환합니다. 각 행은 필드 이름으로 접근 가능한 튜플로 나타납니다. 이는 열 이름으로 데이터에 접근할 수 있으면서도 튜플의 간결함을 유지합니다.

#select
def get_user():
    cursur = connection.cursor()
    sql = "SELECT * FROM users"
    cursur.execute(sql)
    users = cursur.fetchall() #fetchone 1개
    print(users[0]['user_id'])
    cursur.close()

# insert
def add_user():
    cursur = connection.cursor()
    userId = 999
    userName = "조민수"
    email = "minsoo@gmail.com"
    age = 27
    insertSql = f"INSERT INTO users(user_id,user_name,email,age) VALUES ({userId},'{userName}','{email}',{age})"
    cursur.execute(insertSql)
    connection.commit()
    cursur.close()


#update
def update_user():
    cursur = connection.cursor()
    update_name = "조만수"
    sql = f"UPDATE users SET user_name ='{update_name}' WHERE user_id = 999"
    cursur.execute(sql)
    connection.commit()
    cursur.close()

#delete
def delete_user():
    cursur = connection.cursor()
    sql = "DELETE FROM users WHERE user_id = 101"
    cursur.execute(sql)
    connection.commit()
    cursur.close()







