from flask_restful import Resource, abort

from ciphers.CustomParser import Parsely


class Affine(Resource):
    """
    A Simple Affine Cipher. y = mx+b
    """

    def get(self):
        """


        Return:
             The Encoded/Decoded User's message in json format.
        """
        parser = Parsely()
        parser = Parsely.parser_affine()
        args = parser.parse_args()
        inverse = self.check_coprime(args.privateKey, 26)
        print(inverse)
        if args.mode is 0:
            return self.encode(args.message, args.privateKey, args.intercept)
        return self.decode(args.message, inverse, args.intercept)

    def encode(self, user_input, m, b):
        """
        Encode the selected character based off the intercept and coefficient.
        Attributes:
            user_input: The user's message
            m: The coefficient of the picked character
            b: The intercept value.

            Return:
                The encoded value of the given character.
        """
        encoded_input = []
        user_input = user_input.upper()
        for i in range(len(user_input)):
            current_char = user_input[i]
            if 65 <= ord(current_char) <= 90:
                encoded_input.append(chr((((ord(current_char) - 65) * m) + b) % 26 + 65))
            else:
                encoded_input.append(ord(current_char))  ##any other ascii values

        return encoded_input  # list of alphabet values except for spaces etc

    # A*x +m
    def decode(self, encoded, inverse, b):
        """
        Decode the selected character based off the intercept and coefficient.
        unencoded = inverse *(encoded -m)yt

        Attributes:
            encoded: The user's message encoded
            inverse: The inverse of the coefficient.
            b: The intercept value.

            Return:
                The decoded value of the given character.
        """
        decoded = []
        for x in encoded:
            x = ord(x) - 65
            if 0 <= x <= 26:
                zz = ((((inverse * (x - b)) % 26) + 65))
                decoded.append(chr((((inverse * (x - b)) % 26) + 65)))

            else:
                decoded.append(chr(x))

        return decoded  # list of ascii values

    def egcd(self, a, b):
        """
        Extended Euclidean algorithm
        Attributes:
            a:The selected number
            b:The selected modulus

        Return:
            The Greatest Common Denominator.
        """
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.egcd(b % a, a)
            return g, x - (b // a) * y, y

    def modinv(self, a, m):
        """
        https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
        This is to find the multiplicative inverse in order to check if the user provided value is coprime.
        It  only exists when the gcd of a,m are 1.

        Attributes:
            a: The selected number
            m: The selected modulus,26 is the default here.
        Return:
            None or the  multiplicative inverse of the selected number.
        """
        g, x, y = self.egcd(a, m)
        if g != 1:
            return None
        else:
            return x % m

    def check_coprime(self, proposed_value, modolus):
        """
        Could just have a list of values but check if the user provided value
        is coprime with 26.

        Args:
         proposed_value:The user provided value
         modolus: Constant value of 26.

        Returns:
            None if it is coprime otherwise an error message with coprime value.
        """
        possible_value = self.modinv(proposed_value, modolus)
        if possible_value is None:
            coPrimeList = []
            for x in range(modolus):
                res = self.modinv(x, modolus)
                if res is not None:
                    coPrimeList.append(res)
            coPrimeList.sort()
            abort(400, message="Below are the coprime values with 26. Please use one", coprimeValues=coPrimeList)
        return possible_value
