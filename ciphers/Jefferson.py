
import random

from flask import jsonify
from flask_restful import Resource

from ciphers.CustomParser import Parsely


class Jefferson(Resource):
    def get(self):
        """
        This is the method that handles GET Requests for Jefferson wheel Cipher
        Args:
            None since a Custom Parser Object is imported from CustomParser
        Return:
            The output of the encode/decode functions.
        """
        parser = Parsely()
        parser = parser.parser_jeff()
        args = parser.parse_args()
        if args.mode is 0:
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
        This performs the encoding of the cipher text.The shift factor is positive
        to encode the message.

        Args:
            user_input: The message provided to the cipher.
            shift:the line which to read from.
            wheel_order: the order of the 25 wheels.
        Returns:
            The encoded message,shift value and wheel order  in json format.
        """
        cipher = []
        wheel_order = wheel_order.split(",")
        shift %= 26
        user_input = user_input.upper()

        for x in range(len(user_input)):
            x %= 25
            perm = alphabet[int(wheel_order[x])]

            if ord(user_input[x]) <= 64 or ord(user_input[x]) > 90:
                cipher.append(user_input[x])
            else:
                cipher.append(perm[(perm.index(user_input[x]) + shift) % 26])
        return jsonify({"message":''.join(cipher),
                        "wheel_order":self.stringify_wheel(wheel_order),
                        "shift":shift})

    def decode(self, encode_input, shiftFactor, wheel_order):
        """
        This performs the decoding of the message.The shiftfactor is negative
        for decoding.

        Args:
            user_input: The message provided to the cipher.
            shiftFactor: The line which to read the message
            wheel_order: the order of the 25 wheels.
        Returns:
            The decoded message and the wheel order used in json format.
        """
        return self.encode(encode_input, -shiftFactor, wheel_order)

    def check_wheel_parameters(self, wheel_order):
        """
        This is to ensure that user provided wheel order is meets the criteria.
        The wheel order must be values [0-24],no repeats and comma seperated.
        Args:
            wheel_order:
        Returns:
            True if the wheel order is valid otherwise False.
        """
        res = set(wheel_order.split(","))
        for x in res:
            if x.isalpha():
                return False
        if len(res) is not 25:
            return False
        return True

    def stringify_wheel(self,wheel_order):
        """
        To provide the user a copy and paste method to share wheel orders
        Args:
            wheel_order: The order of the provided wheels.
        Returns:
             The wheel order in a comma seperated string
        """
        result = []
        for i in range(len(wheel_order)-1):
            result.append(str(wheel_order[i])+',')
        result.append(str(wheel_order[len(wheel_order)-1]))
        return ''.join(result)


alphabet = ["ABCEIGDJFVUYMHTQKZOLRXSPWN", "ACDEHFIJKTLMOUVYGZNPQXRWSB", "ADKOMJUBGEPHSCZINXFYQRTVWL",
            "AEDCBIFGJHLKMRUOQVPTNWYXZS", "AFNQUKDOPITJBRHCYSLWEMZVXG", "AGPOCIXLURNDYZHWBJSQFKVMET",
            "AHXJEZBNIKPVROGSYDULCFMQTW",  # 6
            "AIHPJOBWKCVFZLQERYNSUMGTDX", "AJDSKQOIVTZEFHGYUNLPMBXWCR", "AKELBDFJGHONMTPRQSVZUXYWIC",
            "ALTMSXVQPNOHUWDIZYCGKRFBEJ", "AMNFLHQGCUJTBYPZKXISRDVEWO", "ANCJILDHBMKGXUZTSWQYVORPFE",
            "AODWPKJVIUQHZCTXBLEGNYRSMF", "APBVHIYKSGUENTCXOWFQDRLJZM", "AQJNUBTGIMWZRVLXCSHDEOKFPY",
            "ARMYOFTHEUSZJXDPCWGQIBKLNV", "ASDMCNEQBOZPLGVJRKYTFUIWXH", "ATOJYLFXNGWHVCMIRBSEKUPDZQ",
            "AUTRZXQLYIOVBPESNHJWMDGFCK", "AVNKHRGOXEYBFSJMUDQCLZWTIP", "AWVSFDLIEBHKNRJQZGMXPUCOTY",
            "AXKWREVDTUFOYHMLSIQNJCPGBZ", "AYJPXMVKBQWUGLOSTECHNZFRID", "AZDNBUHYFWJLVGRCQMPSOEXTKI"]
