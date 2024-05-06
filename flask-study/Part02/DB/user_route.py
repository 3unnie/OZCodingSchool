from flask_smorest import Blueprint, abort
from flask import request

def create_user_blp(mysql):

    user_blp = Blueprint('user_routes', __name__, url_prefix = '/users')

    #전체 유저 get
    @user_blp.route('/', methods = ['GET'])
    def get_users():

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall() #튜플/결과타입

        cursor.close()

        users_list = []
        for user in users:
            users_list.append({
                'id' : user[0],
                'name' : user[1],
                'email' : user[2]
            })
        
        return users_list
    
    @user_blp.route('/', methods = ['POST'])
    def add_user():
        user_data = request.json
  
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user_data['name'], user_data['email']))
        mysql.connection.commit()

        cursor.close()

        return {'msg':'add success'}
    
    @user_blp.route('/<int:user_id>',  methods = ['PUT'])
    def update_user(user_id):
        user_data = request.json
       
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (user_data['name'],user_data['email'],user_id))
        mysql.connection.commit()
        cursor.close()

        return {'msg':'update success'}
    
    @user_blp.route('/<int:user_id>',  methods = ['DELETE'])
    def delete_user(user_id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        mysql.connection.commit()
        cursor.close()

        return {'msg':'delete success'}
    
    return user_blp