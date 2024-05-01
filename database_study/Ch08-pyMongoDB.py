# 설치pip install pymongo
from pymongo import MongoClient

#(1)MongoDB인스턴스에 연결
client = MongoClient('mongodb://localhost:27017/')
# client = MongoClient('mongodb://username:password@localhost:27017/')

#(2)데이터베이스 선택
db = client['pyMongo_study'] #use pyMongo_study'

#(3)콜렉션 선택(없으면 자동 생성)
collection = db['student']

#(4)Create/Read/Update/Delete 접근

#insert
#student1 = {"name": "munji", "age": 1, "sex": "male"}
#collection.insert_one(student1)

#documents 조회(READ)

#collection.find()
for doc in collection.find():
    print(doc)

#조건을 넣어 조회
query = {"name":"munji"}
for doc in collection.find(query):
    print(doc)

#update
collection.update_one({"name":"munji"},{"$set": {"age": 0.9}})

#delete 
collection.delete_one(query)

#콜렉션 삭제
db.drop_collection('student')
