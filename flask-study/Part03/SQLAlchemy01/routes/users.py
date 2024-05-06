from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models.models import User

user_blp = Blueprint('Users', 'users', description = '유저', url_prefix = '/user')

@user_blp.route('/')
class UserList(MethodView):
    def get(self):
        users = User.query.all()
        user_data = [
            {'id' : user.id,
             'name' : user.name,
             'email' : user.email 
            } for user in users
        ]
        return user_data
    
    def post(self):
        data = request.json
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'msg':'성공적으로 등록되엇습니다'}), 201
    
@user_blp.route('/<int:user_id>')
class oneUser(MethodView):

    def get(self,user_id):
        user = User.query.get_or_404(user_id)
        user_data = {'id' : user.id, 'name' : user.name, 'email' : user.email }
       
        return user_data

    def put(self,user_id):
        data = request.json
        user = User.query.get_or_404(user_id)
        user.name = data['name']
        user.email = data['email']
        db.session.commit()

        return jsonify({'msg':'성공적으로 변경되엇습니다'}), 201

    def delete(self,user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({'msg':'성공적으로 삭제되엇습니다'}), 204