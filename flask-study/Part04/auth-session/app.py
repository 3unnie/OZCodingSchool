from flask import Flask,render_template, request, redirect, session, flash
from datetime import timedelta

application = Flask(__name__)

application.secret_key = 'flask-secret-key' #.env or yaml
application.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days = 7)

users = {
    "dust" : "1234",
    "day" : "5678"
}

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/login', methods = ['POST'])
def login():
    id = request.form['username']
    pwd = request.form['password']

    if id in users and users[id] == pwd:
        session['id'] = id
        session.permanent = True
        return redirect('/secret')
    else:
        flash("Invalid id or password")
        return redirect('/')
    
@application.route('/secret')
def secret():
    if 'id' in session:
        return render_template('secret.html')
    else:
        return redirect('/')
    
@application.route('/logout')
def logout():
    session.pop('id', None)
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    application.run(debug=True)