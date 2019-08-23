import unittest
from ciphers import Bacon


class BaconTest(unittest.TestCase):
    def test_encode(self):
        secret_msg = "steamroller"
        plain_text = "hello my darling would you like for me to buy milk from the store I am heading back from work if you didnt already grab it I am sleeping on the couch with my lovely zooot suit and dog"
        crispy = Bacon.Bacon()
        encoded_msg = crispy.encode(secret_msg, plain_text)
        correct_enc = "HelLo My dARliNg would yoU LikE for Me TO Buy MiLK fRoM The StoRe i aM HEADING BACK FROM WORK IF YOU DIDNT ALREADY GRAB IT I AM SLEEPING ON THE COUCH WITH MY LOVELY ZOOOT SUIT AND DOG"
        print(encoded_msg)
        self.assertEqual(encoded_msg, correct_enc)

    def test_decode(self):
        encoded_msg = "HelLo My dARliNg would yoU LikE for Me TO Buy MiLK fRoM The StoRe i aM HEADING BACK FROM WORK IF YOU DIDNT ALREADY GRAB IT I AM SLEEPING ON THE COUCH WITH MY LOVELY ZOOOT SUIT AND DOG"
        crispy = Bacon.Bacon()
        decoded_msg = crispy.decode(encoded_msg)
        self.assertEqual(decoded_msg, "STEAMROLLER__________________")
