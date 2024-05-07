from flask import request, jsonify
from flask_smorest import Blueprint, abort

def create_posts_blp(mysql):
    posts_blp = Blueprint("posts", __name__, description='posts api', url_prefix='/posts')

    #API CRUD
    @posts_blp.route('/', methods=['GET', 'POST'])
    def post():
        cursor = mysql.connection.cursor()
        #게시글 조회
        if request.method == "GET":
            sql = "SELECT * FROM posts"
            cursor.execute(sql)
            posts = cursor.fetchall()
            cursor.close()

            post_list = []
            for post in posts:
                post_list.append({
                    'id': post[0],
                    'title' : post[1],
                    'content' : post[2],
                    'created_at' : post[3]
                })
            return post_list
        
        #게시글 생성
        elif request.method == "POST":
            title = request.json.get('title')
            content = request.json.get('content')
            
            if not title or not content:
                abort(400, message = "[Warn]Title/Content cannot be empty")
            
            sql = "INSERT INTO posts(title, content) VALUES (%s, %s)"
            cursor.execute(sql,(title, content))
            mysql.connection.commit()

            return jsonify({'msg' : "[Msg]Successfully created post"}), 201
        
    @posts_blp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def OnePost(id):
        cursor = mysql.connection.cursor()
        #특정 게시글 조회
        if request.method == "GET":
            sql = f"SELECT * FROM posts WHERE id = {id}"
            cursor.execute(sql)
            post = cursor.fetchone()
            
            if not post:
                abort(404, message = "[Warn]Post is Not exist")

            cursor.close()

            post_json = {
                'id': post[0],
                'title' : post[1],
                'content' : post[2],
                'created_at' : post[3]
            }

            return post_json

        #특정 게시글 수정 
        elif request.method == "PUT":
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, message = "[Warn]Title/Content cannot be empty")

            sql = "UPDATE posts SET title=%s, content=%s WHERE id=%s"
            cursor.execute(sql, (title, content, id))
            mysql.connection.commit()

            return jsonify({'msg' : "[Msg]Successfully updated post"}), 201


        #특정 게시글 삭제
        elif request.method == "DELETE":
            sql = "DELETE FROM posts WHERE id=%s"
            cursor.execute(sql,(id,))
            mysql.connection.commit()

            return jsonify({'msg' : "[Msg]Successfully deleted post"}), 204
    
    return posts_blp
