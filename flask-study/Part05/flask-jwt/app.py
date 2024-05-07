from flask import Flask, render_template
from flask_jwt_extended import JWTManager
from routes.user import user_blp

application = Flask(__name__)
application.config['JWT_SECRET_KEY'] = 'secret_key'

jwt = JWTManager(application)

application.register_blueprint(user_blp, url_prefix='/user')

@application.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    application.run()