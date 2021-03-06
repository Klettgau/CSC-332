from flask import Blueprint
from flask_restful import Api
from ciphers.Engima import M3
from ciphers.Vigenere import Vig
from ciphers.Affine import Affine
from ciphers.Julius import Julius
from ciphers.Jefferson import Jefferson
#from ciphers.Hill import  Hill
from application.Dummy import mokcing
engima_blue = Blueprint('enigma',__name__)
api = Api(engima_blue)
api.add_resource(mokcing,'/cipherList')
api.add_resource(M3,'/Enigma')
api.add_resource(Vig,'/Vigenere')
api.add_resource(Affine,'/Affine')
api.add_resource(Julius,'/Julius')
api.add_resource(Jefferson,'/Jefferson')
#api.add_resource(Hill, '/Hill')
