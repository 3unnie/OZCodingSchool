from flask import Flask, request
from routes import register_routes

application = Flask(__name__)

register_routes(application)

if __name__ == '__main__':
    application.run(debug=True)