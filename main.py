from flask import Flask, redirect, request, Response, jsonify, url_for, render_template
from flask_restful import Resource, Api
import ciphers.CustomParser
import ciphers.Engima
from blueprint import engima_blue,vig_blue


app= Flask(__name__)
app.register_blueprint(engima_blue)
api= Api(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
