from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    data={
        'name':'munji',
        'age':1,
        'is_admin': True,
        'item_list':['아이템1','아이템2','아이템3']
    }
    #렌더링할 html 파일명, html이 받을 data

    return render_template('index.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)