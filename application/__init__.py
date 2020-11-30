from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
from ciphers import CiphersBp
def create_app():
    app = Flask(__name__)

    with app.app_context():
        app.register_blueprint(CiphersBp.engima_blue)
        CORS(app)
        Api(app)
    return app