# chr int to char
# ord char to int
from flask_restful import Resource
from ciphers.CustomParser import Parsely
alphabet = ["abcdefghijklmnopqrstuvwxyz"]

class Julius(Resource):
    def get(self):
        parser = Parsely.parser_jules(Parsely)
        args =parser.parse_args()
        if args.mode is 0:
            print("hit")
            return self.encode(args.message,args.privateKey)
        return self.decode(args.message,args.privateKey)


    def encode(self,plain_text, key):
        listPlainTest = list(plain_text.upper())
        encoded_text_list = ''
        key %=26
        for x in listPlainTest:
            x = ord(x)-65
            if x >-1 and x<26:
               encoded_text_list= encoded_text_list+(chr(((x+key)%26)+65))
            else:
                encoded_text_list=encoded_text_list+chr(x+65)
        return encoded_text_list

    def decode(self,encoded, key):
        decoded_list = ''
        encoded = encoded.upper()
        key %=26
        for x in encoded:
            x= ord(x) -65
            if x>-1 and x<26:
               decoded_list= decoded_list+(chr(((x-key)%26)+65))
            else:
                decoded_list=decoded_list+(chr(x-65))
        return decoded_list

