from flask import Flask, render_template
from flask_httpauth import HTTPBasicAuth

application = Flask(__name__)

auth = HTTPBasicAuth()

users = {
    'admin' : 'secret',
    'guest' : 'pw1234'
}

@application.route('/')
def index():
    return render_template('index.html')

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    
@application.route('/protected')
@auth.login_required
def protected():
    return render_template('secret.html')

if __name__ == "__main":
    application.run(debug=True)