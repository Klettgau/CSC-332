from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api

def create_app():
    app = Flask(__name__,instance_relative_config=False)

    with app.app_context():
        app.register_blueprint()
        CORS(app)
        Api(app)
    return app