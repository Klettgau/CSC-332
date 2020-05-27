from flask_restful import Resource

from deprecated.CustomParser import Parsely


class Vig(Resource):
    def get(self):
        parser= Parsely()
        parser=parser.parser_vig()
        args = parser.parse_args()
        if args.mode is 0:
            return self.encode(args.message,args.privateKey)
        else:
            return self.decode(args.message,args.privateKey)




    def print_tabula(self):
        """
        Print out a reference tabula recta.

        Returns:
             A Tabula Recta in String format.
        """
        recta = []
        for i in range(0, 26):
            line = ''
            for ii in range(0, 26):
                line = line + (chr(65 + ((ii + i) % 26)))
            recta.append(line)
        return recta

    def encode(self,plainext, keyword):
        """
        Encode the message using the supplied values.
        The key dictates the row to use and the plaintext dictates the column.
        Args:
            plainext:The message to be encoded.
            keyword: The private key to be used for the message.
        Returns:
            The encoded message using the provided values.
        """

        cipher_text = []
        for c in range(len(plainext)):
            cipher_text.append(chr((((ord(plainext[c]) - 65) + (ord(keyword[c % len(keyword)]) - 65)) % 26) + 65))
        return cipher_text

    def decode(self,cipher, keyword):
        """
        Same as Encoding but subtract the key from the cipher text.
        """
        plain = []
        for c in range(len(cipher)):
            plain.append(chr((((ord(cipher[c]) - 65) - (ord(keyword[c % len(keyword)]) - 65)) % 26) + 65))

        return plain
