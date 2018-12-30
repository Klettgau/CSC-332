## so you always start at line 1 but the key is the amount you go to the right
# be able to pick the line to start with
from flask_restful import Resource
from ciphers.CustomParser import Parsely


class Jefferson(Resource):
    def get(self):
        parser = Parsely.parser_jeff(Parsely)
        args = parser.parse_args()
        if args.mode is 0:
            if args.wheel_order is None:
                return self.encode(args.message, args.privateKey, self.not_random())

            return self.encode(args.message, args.privateKey, self.wheel_order)
        else:
            return self.decode(args.message, args.privateKey, self.wheel_order)

    def encode(self, userInput, shift, wheel_order):
        """
        This is a test for jeff

        Args:
            userInput:String
            shift:the starting wheel

        Returns:
        """
        cipher = []
        shift %= 26
        userInput = userInput.upper()

        # the negative equivalent decrpyts its so encrupt l--R and decrypt R--L
        for x in range(len(userInput)):
            x%=25
            # wheel = alphabet[x]  # iterate over all the wheels
            print(wheel_order)
            try:
                perm = alphabet[wheel_order[x]]
                print("shift",shift,perm,x)
            except IndexError:
                print(type(x),"x value--------------------------------------------",x)
            # 65-90 Capital otherwise just return the value
            if ord(userInput[x]) <= 64:
                cipher.append(userInput[x])
            elif ord(userInput[x]) > 90:
                cipher.append(userInput[x])
            else:
                #print("the encoded char:",perm[(perm.index(userInput[x]) + shift)%26])
                cipher.append(perm[(perm.index(userInput[x]) + shift)%25])
                # cipher.append(wheel[(wheel.index(userInput[x]) + shift) % 26])  ##26 is the len of the wheel
        return {''.join(cipher): wheel_order}

    def decode(self, encodeInput, shiftFactor, wheel_order):
        # colors may not work for all platforms
        return self.encode(encodeInput, -shiftFactor, wheel_order)

    def check_parameters(self,wheel_order):
        # we check that the rotor order is unique and a set of 25
        res = set(wheel_order.split(","))
        if len(res) is not 25:
            return False
        return True

    def check_digit(self,wheel_order):
        return(wheel_order..isdigit())


    def not_random(self):
        import random
        from time import process_time

        # print(time.localtime())
        setty = list()
        res = list()
        for x in range(25):
            setty.append(x)
        for y in range(25):
            tmp = random.randint(0, 25)
            x = False
            while (not x):
                if setty.__contains__(tmp):
                    res.append(setty.pop(setty.index(tmp)))
                    x = True

                tmp = random.randint(0, 25)
        return res


alphabet = ["ABCEIGDJFVUYMHTQKZOLRXSPWN", "ACDEHFIJKTLMOUVYGZNPQXRWSB", "ADKOMJUBGEPHSCZINXFYQRTVWL",
            "AEDCBIFGJHLKMRUOQVPTNWYXZS", "AFNQUKDOPITJBRHCYSLWEMZVXG", "AGPOCIXLURNDYZHWBJSQFKVMET",
            "AHXJEZBNIKPVROGSYDULCFMQTW",  # 6
            "AIHPJOBWKCVFZLQERYNSUMGTDX", "AJDSKQOIVTZEFHGYUNLPMBXWCR", "AKELBDFJGHONMTPRQSVZUXYWIC",
            "ALTMSXVQPNOHUWDIZYCGKRFBEJ", "AMNFLHQGCUJTBYPZKXISRDVEWO", "ANCJILDHBMKGXUZTSWQYVORPFE",
            "AODWPKJVIUQHZCTXBLEGNYRSMF", "APBVHIYKSGUENTCXOWFQDRLJZM", "AQJNUBTGIMWZRVLXCSHDEOKFPY",
            "ARMYOFTHEUSZJXDPCWGQIBKLNV", "ASDMCNEQBOZPLGVJRKYTFUIWXH", "ATOJYLFXNGWHVCMIRBSEKUPDZQ",
            "AUTRZXQLYIOVBPESNHJWMDGFCK", "AVNKHRGOXEYBFSJMUDQCLZWTIP", "AWVSFDLIEBHKNRJQZGMXPUCOTY",
            "AXKWREVDTUFOYHMLSIQNJCPGBZ", "AYJPXMVKBQWUGLOSTECHNZFRID", "AZDNBUHYFWJLVGRCQMPSOEXTKI"]
