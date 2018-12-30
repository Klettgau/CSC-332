from flask_restful import Resource
from ciphers.CustomParser import Parsely

class Vig(Resource):
    def get(self):
        parser=Parsely.parser_vig(Parsely)
        args = parser.parse_args()
        if args.mode is 0:
            return self.encode(args.message,args.privateKey)
        else:
            return self.decode(args.message,args.privateKey)




    def print_tabula(self):
        recta = []
        for i in range(0, 26):
            line = ''
            for ii in range(0, 26):
                line = line + (chr(65 + ((ii + i) % 26)))
            recta.append(line)
        return recta

    def encode(self,plainext, keyword):
        #  key(row) column(plaintext)
        cipher_text = []
        for c in range(len(plainext)):
            cipher_text.append(chr((((ord(plainext[c]) - 65) + (ord(keyword[c % len(keyword)]) - 65)) % 26) + 65))
        return cipher_text

    def decode(self,cipher, keyword):
        tabula = self.print_tabula()  # list of lists that are the tabula
        plain = []
        for c in range(len(cipher)):
            plain.append(chr((((ord(cipher[c]) - 65) - (ord(keyword[c % len(keyword)]) - 65)) % 26) + 65))

        return plain
