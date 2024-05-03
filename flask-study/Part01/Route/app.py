from flask import Flask,request,Response

app = Flask(__name__)

host = '127.0.0.1'
port = '5000'

@app.route('/')
def home():
    return 'Main Page'

@app.route('/about')
def about():
    return 'About Us'

#동적으로 url파라미터 값을 받아서 처리
@app.route('/user/<userId>')
def user_profile(userId):
    return f'Hello {userId}'

@app.route('/number/<int:number>')
def num(number):
    return f'숫자는 {number}'

#POST요청
import requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    test = 'poooooooooooooooost'
    response = requests.post(url = url,data = test)

    return response

@app.route('/submit',methods=['GET','POST','PUT','DELETE'])
def submit():
    if request.method == 'GET':
        print('GET 방식')

    if request.method == 'POST':
        print('POST 방식',request.data)

    if request.method == 'PUT':
        print('PUT 방식')

    if request.method == 'DELETE':
        print('DELETE 방식')
    return Response('성공=====================', status=200)


if __name__ == "__main__":
    #app.run(host=host,port=port)
    print()
