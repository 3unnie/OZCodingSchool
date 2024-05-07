from flask import Flask, render_template, request, redirect, url_for

application = Flask(__name__)

users = [
    {"username": "dust", "name": "munji"},
    {"username": "day", "name": "haru"},
    {"username": "eunnie", "name": "eunnie"}
]

@application.route('/')
def index():
    return render_template('index.html', users=users)


@application.route('/add', methods=['GET', 'POST'])
def add_user():
    # user 추가
    if request.method == 'POST':

        username = request.form['username']
        name = request.form['name']

        users.append({'username': username, 'name': name})
        
        return redirect(url_for('index'))
   
    return render_template('add_user.html')

@application.route('/edit/<username>', methods=['GET', 'POST'])
def edit_user(username):
    # user 수정 
    user = next((user for user in users if user['username'] == username), None)

    if not user:
        return redirect(url_for('index'))

    if request.method == 'POST':
        user['name'] = request.form['name']
        return redirect(url_for('index'))

    return render_template('edit_user.html', user=user)

@application.route('/delete/<username>')
def delete_user(username):
    # user 삭제
    global users

    users = [user for user in users if user['username'] != username]
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    application.run(debug=True)
