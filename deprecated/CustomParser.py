# this is to create individual parsers for the main class
from flask_restful import reqparse


class Parsely:
    """
    Deprecated
    """

    def parser_jules(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("message", type=str, required=True, help="the message")
        parser.add_argument("privateKey", required=True, help="the private key.", type=int)
        parser.add_argument("mode", required=True, help="0 for encode and 1 for decode", type=int)
        return parser

    def parser_affine(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("message", type=str, required=True, help="the message")
        parser.add_argument("privateKey", required=True, help="this is the m in y=mx+b", type=int)
        parser.add_argument("intercept", required=True, help="this is the b in linear y=mx+b", type=int)
        parser.add_argument("mode", required=True, help="0 for encode and 1 for decode", type=int)
        return parser

    def parser_vig(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("message", type=str, required=True, help="the message")
        parser.add_argument("privateKey", required=True, help="this is a string used to encode/decode the message")
        parser.add_argument("mode", required=True, help="0 for encode and 1 for decode", type=int)
        return parser

    def parser_jeff(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("message", type=str, required=True, help="the message")
        parser.add_argument("privateKey", required=True, type=int)
        parser.add_argument("wheel_order", required=True)
        parser.add_argument("mode", required=True, help="0 for encode and 1 for decode", type=int)
        return parser

    def parser_enigma(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("message", type=str, required=True, help="the message")
        parser.add_argument("stecker_pair", type=str, required=True)
        parser.add_argument("ring_setting", type=str, required=True)
        parser.add_argument("rotor_order", type=str, required=True)
        parser.add_argument("start_position", type=str, required=True)
        return parser

    def parser_hill(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("message", type=str, required=True, help="the user provided message.")
        parser.add_argument("mode", type=int, required=True, help="0 to  encode the message and 1 to decode the message.")
        parser.add_argument("key", type=int, help="sequence of integers that defines the private key.")
        parser.add_argument("dimension",type=int,help="the dimension of the key matrix.")
        return parser
