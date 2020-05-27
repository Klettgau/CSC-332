# chr int to char
# ord char to int
from flask_restful import Resource

from deprecated.CustomParser import Parsely


class Julius(Resource):

    def get(self):
        parser = Parsely()
        parser = parser.parser_jules()
        args = parser.parse_args()
        if args.mode is 0:
            return self.encode(args.message, args.privateKey)
        return self.decode(args.message, args.privateKey)

    def encode(self, plain_text, key):
        plain_text_mod = list(plain_text.upper())
        encoded_text_list = ''
        key %= 26
        for x in plain_text_mod:
            x = ord(x) - 65
            if 0 <= x < 26:
                encoded_text_list = encoded_text_list + (chr(((x + key) % 26) + 65))
            else:
                encoded_text_list = encoded_text_list + chr(x + 65)
        return encoded_text_list

    def decode(self, encoded, key):
        decoded = ''
        encoded = encoded.upper()
        key %= 26
        for x in encoded:
            x = ord(x) - 65
            if 0 <= x < 26:
                decoded = decoded + (chr(((x - key) % 26) + 65))
            else:
                decoded = decoded + (chr(x - 65))
        return decoded
