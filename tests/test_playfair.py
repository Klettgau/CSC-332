import unittest
from ciphers import Playfair as pf
import ciphers.Utils as util


class PlayFairTest(unittest.TestCase):

    def test_double_dection(self):
        base_msg="MOSESSUPPOSES"
        updated_msg=pf.detect_double(util.char_to_int(base_msg))
        print(updated_msg)
        self.assertEqual(len(updated_msg),7)

    # def test_which_rule(self):
    #
    def test_rule1(self):
        # Only called when input has same letter in a row
        # Assumes empty strings etc are handled upstream
        golden_a=(23,23)
        golden_b=(0,23)
        first_msg = util.char_to_int("X")
        second_msg = util.char_to_int("A")

        first_mod = pf.rule_one(first_msg)
        second_mod = pf.rule_one(second_msg)
        self.assertEqual(len(first_mod), 2)
        self.assertEqual(golden_a,first_mod)

        self.assertEqual(len(second_mod), 2)
        self.assertEqual(golden_b,second_mod)

    # def test_rule2(self):
    #
    # def test_rule3(self):
    #
    # def test_rule4(self):
    #
    # def test_key_matrix(self):
