from flask import Flask, jsonify, request

app = Flask(__name__)


#전체 게시글
# @app.route('/api/v1/feeds', methods = ['GET'])
# def show_all_feeds():
#     data = {
#         'result':'success',
#         'data':{
#             'feed1':'data1',
#             'feed2':'data2',
#             'feed3':'data3'        
#         }
#     }
#     return data

#특정 게시글
@app.route('/api/v1/feeds/<int:feed_id>', methods = ['GET'])
def show_feed(feed_id):

    print(feed_id)
    data = {
        'result':'success',
        'data':{
            'feed1':'data1',       
        }
    }
    return data

#게시글 작성
@app.route('/api/v1/feeds', methods = ['POST'])
def create_feed():
    name = request.form['name']
    age = request.form['age']

    print(name,age,'*************************************')

    return jsonify({'result':'success'})

