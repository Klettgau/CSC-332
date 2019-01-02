## so you always start at line 1 but the key is the amount you go to the right
# be able to pick the line to start with
from flask_restful import Resource
from flask import jsonify
from ciphers.CustomParser import Parsely
import random


class Jefferson(Resource):
    def get(self):
        """
        This is the method that handles GET Requests for Jefferson wheel Cipher
        Args:
            None since a Custom Parser Object is imported from CustomParser
        Return:
            The output of the encode and decode functions.
        """
        parser = Parsely.parser_jeff(Parsely)
        args = parser.parse_args()
        if args.mode is 0:
            print(args.wheel_order,"ads")
            if not args.wheel_order:
                return self.encode(args.message, args.privateKey,random.sample(range(0,25),25))
            else:
                if self.check_wheel_parameters(args.wheel_order):
                    return self.encode(args.message, args.privateKey, args.wheel_order)
                return {"error":"the provided wheel order was not valid"}
        else:
            if self.check_wheel_parameters(args.wheel_order):
                return self.decode(args.message, args.privateKey, args.wheel_order)
            return {"error":"the provided wheel order was not valid"}
    def encode(self, user_input, shift, wheel_order):
        """
        This performs the encoding/decoding of the cipher text.

        Args:
            user_input: The message provided to the cipher.
            shift:the line which to read from.
            wheel_order: the order of the 25 wheels.
        Returns:
            The encoded/decoded message,wheel order and line in json format.
        """
        cipher = []
        #wheel_order = wheel_order.split(",")
        shift %= 26
        user_input = user_input.upper()

        # the negative equivalent decrpyts its so encrupt l--R and decrypt R--L
        for x in range(len(user_input)):
            x %= 25
            perm = alphabet[int(wheel_order[x])]

            if ord(user_input[x]) <= 64 or ord(user_input[x]) > 90:
                cipher.append(user_input[x])
            else:
                cipher.append(perm[(perm.index(user_input[x]) + shift) % 26])
        return jsonify({''.join(cipher): wheel_order})

    def decode(self, encode_input, shiftFactor, wheel_order):
        return self.encode(encode_input, -shiftFactor, wheel_order)

    def check_wheel_parameters(self, wheel_order):
        # we check that the rotor order is unique and a set of 25
        res = set(wheel_order.split(","))
        for x in res:
            if x.isalpha():
                return False
        if len(res) is not 25:
            return False
        return True



alphabet = ["ABCEIGDJFVUYMHTQKZOLRXSPWN", "ACDEHFIJKTLMOUVYGZNPQXRWSB", "ADKOMJUBGEPHSCZINXFYQRTVWL",
            "AEDCBIFGJHLKMRUOQVPTNWYXZS", "AFNQUKDOPITJBRHCYSLWEMZVXG", "AGPOCIXLURNDYZHWBJSQFKVMET",
            "AHXJEZBNIKPVROGSYDULCFMQTW",  # 6
            "AIHPJOBWKCVFZLQERYNSUMGTDX", "AJDSKQOIVTZEFHGYUNLPMBXWCR", "AKELBDFJGHONMTPRQSVZUXYWIC",
            "ALTMSXVQPNOHUWDIZYCGKRFBEJ", "AMNFLHQGCUJTBYPZKXISRDVEWO", "ANCJILDHBMKGXUZTSWQYVORPFE",
            "AODWPKJVIUQHZCTXBLEGNYRSMF", "APBVHIYKSGUENTCXOWFQDRLJZM", "AQJNUBTGIMWZRVLXCSHDEOKFPY",
            "ARMYOFTHEUSZJXDPCWGQIBKLNV", "ASDMCNEQBOZPLGVJRKYTFUIWXH", "ATOJYLFXNGWHVCMIRBSEKUPDZQ",
            "AUTRZXQLYIOVBPESNHJWMDGFCK", "AVNKHRGOXEYBFSJMUDQCLZWTIP", "AWVSFDLIEBHKNRJQZGMXPUCOTY",
            "AXKWREVDTUFOYHMLSIQNJCPGBZ", "AYJPXMVKBQWUGLOSTECHNZFRID", "AZDNBUHYFWJLVGRCQMPSOEXTKI"]
