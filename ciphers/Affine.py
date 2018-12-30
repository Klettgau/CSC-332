from flask_restful import Resource,abort
from ciphers.CustomParser import Parsely
# y = mx+b
class Affine(Resource):
    def get(self):
        parser=Parsely.parser_affine(Parsely)
        args = parser.parse_args()
        self.checkCoPrime(args.privateKey,26)
        if args.mode is 0:
            return self.encode(args.message,args.privateKey,args.intercept)
        return self.decode(args.message,args.privateKey,args.intercept)

    def encode(self,user_input, m, b):
        encoded_input = []
        user_input = user_input.upper()
        for i in range(len(user_input)):
            current_char = user_input[i]
            if 65 <= ord(current_char) <= 90:
                encoded_input.append(chr((((ord(current_char) - 65) * m) + b) % 26+65))
            else:
                encoded_input.append(ord(current_char))  ##any other ascii values

        return encoded_input  # list of alphabet values except for spaces etc


    # A*x +m
    def decode(self,encoded, inverse, b):
        # unencoded = inverse *(encoded -m)yt
        decoded = []
        for x in encoded:
            x = ord(x)-65
            if 0 <= x <= 26:
                zz = ((((inverse * (x - b)) % 26) + 65))
                decoded.append(chr((((inverse * (x - b)) % 26) + 65)))

            else:
                decoded.append(chr(x))

        return decoded  # list of ascii values



    # https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
    # the link to the source for the egcd and modinv function.I got lazy

    def egcd(self,a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.egcd(b % a, a)
            return g, x - (b // a) * y, y


    def modinv(self,a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            return None
        else:
            return x % m


    # this is mine
    def checkCoPrime(self,proposed_value, modolus):
        possible_value = self.modinv(proposed_value, modolus)
        if possible_value is None:
            coPrimeList = []
            for x in range(modolus):
                res = self.modinv(x, modolus)
                if res is not None:
                    coPrimeList.append(res)
            coPrimeList.sort()
            abort(400,message="Below are the coprime values with 26. Please use one",coprimeValues=coPrimeList)
