# this is to create individual parsers for the main class
import argparse
from flask_restful import reqparse


class Parsely:
    def parser_jules(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("message", type=str, required=True, help="the message")
        parser.add_argument("privateKey", required=True, help="the private key.",type=int)
        parser.add_argument("mode",required=True,help="0 for encode and 1 for decode",type=int)
        return parser

    def parser_affine(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("message", type=str, required=True, help="the message")
        parser.add_argument("privateKey", required=True, help="this is the m in y=mx+b",type=int)
        parser.add_argument("intercept", required=True,help="this is the b in linear y=mx+b", type=int)
        parser.add_argument("mode",required=True,help="0 for encode and 1 for decode",type=int)
        return parser

    def parser_vig(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("message", type=str, required=True, help="the message")
        parser.add_argument("privateKey", required=True,help="this is a string used to encode/decode the message")
        parser.add_argument("mode",required=True,help="0 for encode and 1 for decode",type=int)
        return parser

    def parser_jeff(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("message", type=str, required=True, help="the message")
        parser.add_argument("privateKey", required=True, type=int)
        parser.add_argument("wheel_order")
        parser.add_argument("mode",required=True,help="0 for encode and 1 for decode",type=int)
        return parser

    def Enigma(self):
        parser = reqparse.RequestParser(bundle_errors=True)
        parser.add_argument("message", type=str, required=True, help="the message")
        parser.add_argument("stecker_pair", type=str, required=True)
        parser.add_argument("ring_setting", type=str, required=True)
        parser.add_argument("rotor_order", type=str, required=True)
        parser.add_argument("start_position", type=str, required=True)
        return parser
