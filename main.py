from flask import Flask
from flask_restful import Resource, Api
from blueprint import engima_blue


app= Flask(__name__)
app.register_blueprint(engima_blue)
api= Api(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
