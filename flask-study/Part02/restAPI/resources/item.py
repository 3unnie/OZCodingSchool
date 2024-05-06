from flask import request
from flask_restful import Resource

items = []

class Item(Resource):

    #조회
    def get(self,name):
        for item in items:
            if item['name'] == name:
                return item
        
        return {"msg" : "Item Not Found"}, 404

    #생성
    def post(self, name):
        for item in items:
            if item['name'] == name:
                return {"msg" : "Already Exists"}, 400
        
        data  = request.get_json()
        new_item = {'name': data['name'], 'price' : data['price']}
        items.append(new_item)

        return new_item
    
    #업데이트
    def put(self,name):

        data = request.get_json()

        for item in items:
            if item['name'] == name:
                item['price'] = data['price']
                return item
        
        new_item = self.post(self, name)

        return new_item

    #삭제
    def delete(self,name):
        global items

        items = [item for item in items if item['name'] != name]
        return {'msg':"Item delete"}
