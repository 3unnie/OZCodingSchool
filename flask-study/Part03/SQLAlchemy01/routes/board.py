from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models.models import Board

board_blp = Blueprint('Boards', 'boards', description='게시글', url_prefix='/board')


@board_blp.route('/')
class BoardList(MethodView):
    #전체 게시글 조회
    def get(self):
        boards = Board.query.all() 
        return jsonify([{'id':board.id, 'title':board.title, 'content':board.content, 'author_name': board.author.name} for board in boards])
    
    #게시글 작성
    def post(self):
        data = request.json
        new_boards = Board(title=data['title'], content=data['content'], user_id=data['user_id'])
        db.session.add(new_boards)
        db.session.commit()
        return jsonify({'msg':'게시글이 성공적으로 등록되엇습니다'}), 201

@board_blp.route('/<int:board_id>')
class OneBoard(MethodView):

    #하나의 게시글 불러오기
    def get(self, board_id):
        board = Board.query.get_or_404(board_id)
        return jsonify({'id':board.id, 'title':board.title, 'content':board.content, 'author_name': board.author.name})

    #특정 게시글 수정
    def put(self, board_id):
        board = Board.query.get_or_404(board_id)   
        data = request.json

        board.title = data['title']
        board.content = data['content']

        db.session.commit()

        return jsonify({'msg':'게시글이 성공적으로 수정되엇습니다'}), 201

    #특정 게시글 삭제
    def delete(self, board_id):
        board = Board.query.get_or_404(board_id)
        db.session.delete(board)
        db.session.commit()

        return jsonify({'msg':'게시글이 성공적으로 삭제되엇습니다'}), 204
