from flask import Flask, render_template
from flask_smorest import Api
from flask_mysqldb import MySQL
import yaml
from posts_routes import create_posts_blp

application = Flask(__name__)

db_info = yaml.load(open('db.yaml'), Loader = yaml.FullLoader)

#mysql 연동
application.config['MYSQL_HOST'] = db_info['mysql_host']
application.config['MYSQL_USER'] = db_info['mysql_user']
application.config['MYSQL_PASSWORD'] = db_info['mysql_password']
application.config['MYSQL_DB'] = db_info['mysql_db']

mysql = MySQL(application)

#blp 설정
application.config["API_TITLE"] = "Blog API"
application.config["API_VERSION"] = "1.0"
application.config["OPENAPI_VERSION"] = "3.1.3"
application.config["OPENAPI_URL_PREFIX"] = "/"
application.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
application.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(application)

posts_blp = create_posts_blp(mysql)
api.register_blueprint(posts_blp)

#render_template
@application.route('/manage_blogs')
def manage_blogs():
    return render_template('posts.html')

if __name__ == "__main__":
    application.run(debug=True)