from application import create_app
from flask_restful import Resource
from flask import jsonify
app = create_app()


#this would normally have nginx or guincorn launch it
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000,debug=True)
