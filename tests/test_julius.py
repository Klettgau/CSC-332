import unittest
from ciphers import Julius

class JuliusTest(unittest.TestCase):

    def test_encode(self):
        msg = "drinkwater"
        true_encoded= "qevaxjngre".upper()
        et_tu = Julius.Julius()
        key=13
        test_encoded=et_tu.encode(msg,key)
        self.assertEqual(true_encoded,test_encoded,"these two encoded messages should be equal.")

    def test_decode(self):
        msg = "drinkwater".upper()
        true_encoded= "qevaxjngre".upper()
        et_tu = Julius.Julius()
        key=13
        test_decoded = et_tu.decode(true_encoded,key)
        self.assertEqual(msg,test_decoded,"these two decoded messages should be equal")
