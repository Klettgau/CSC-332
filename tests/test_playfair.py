import unittest
from ciphers import Playfair as pf
import ciphers.Utils as util

class PlayFairTest(unittest.TestCase):

    def test_pad_message(self):
        first_msg=util.char_to_int("")
        second_msg=util.char_to_int("spaceforce")
        third_msg=util.char_to_int("one")
        fourth_msg=util.char_to_int("I")
        first_mod=pf.pad_message(first_msg)
        self.assertEqual(len(first_mod),2)
        second_mod = pf.pad_message(second_msg)
        self.assertEqual(len(second_mod),10)
        third_mod = pf.pad_message(third_msg)
        self.assertEqual(len(third_mod),4)
        four_mod = pf.pad_message(fourth_msg)
        self.assertEqual(len(four_mod),2)

    # def test_which_rule(self):
    #
    def test_rule1(self):
        #Only called when input has same letter in a row
        #Assumes empty strings etc are handled upstream
        first_msg=util.char_to_int("x")
        second_msg=util.char_to_int("A")

        first_mod=pf.rule_one(first_msg)
        second_mod =pf.rule_one(second_msg)
        self.assertEqual(len(first_mod),2)
        self.assertEqual(len(second_mod),2)

    # def test_rule2(self):
    #
    # def test_rule3(self):
    #
    # def test_rule4(self):
    #
    # def test_key_matrix(self):

