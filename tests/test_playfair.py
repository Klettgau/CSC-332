import unittest
from ciphers import Playfair as pf
import ciphers.Utils as util
import numpy as np


class PlayFairTest(unittest.TestCase):

    def test_double_dection(self):
        base_msg = "MOSESSUPPOSES"
        updated_msg = pf.detect_double(util.char_to_int_li(base_msg))
        print(updated_msg)
        self.assertEqual(len(updated_msg), 7)

    def test_which_rule(self):
        # need to rename
        decrypt = True
        encrypt = False
        key_mat = pf.create_key_matrix(5, util.char_to_int_li("CRITER"))
        rule_4 = "APPLEX"
        rule_4_golden = "BOQKIZ"
        rule_3 = "KWYTGNCH"
        rule_3_golden = "PRTFNUAO"
        rule_2 = "UOBDTEWZ"
        rule_2_golden = "OPDFECXV"
        results = list()

        msg_ints = util.char_to_int_li(rule_4)
        padded_msg = pf.detect_double(msg_ints)
        for tup in padded_msg:
            results.append(pf.determine_which_rule(tup, key_mat, 5, encrypt))
        self.assertSequenceEqual(rule_4_golden, util.list_tuples_to_str(results, True))
        results.clear()

        msg_ints = util.char_to_int_li(rule_3)
        padded_msg = pf.detect_double(msg_ints)
        for tup in padded_msg:
            results.append(pf.determine_which_rule(tup, key_mat, 5, encrypt))
        self.assertSequenceEqual(rule_3_golden, util.list_tuples_to_str(results, True))
        results.clear()

        msg_ints = util.char_to_int_li(rule_2)
        padded_msg = pf.detect_double(msg_ints)
        for tup in padded_msg:
            results.append(pf.determine_which_rule(tup, key_mat, 5, encrypt))
        self.assertSequenceEqual(rule_2_golden, util.list_tuples_to_str(results, True))
        results.clear()

        #tests the decrpyt case
        msg_ints = util.char_to_int_li(rule_4_golden)
        padded_msg = pf.detect_double(msg_ints)
        for tup in padded_msg:
            results.append(pf.determine_which_rule(tup, key_mat, 5, decrypt))
        self.assertSequenceEqual(rule_4, util.list_tuples_to_str(results, True))
        results.clear()

        msg_ints = util.char_to_int_li(rule_3_golden)
        padded_msg = pf.detect_double(msg_ints)
        for tup in padded_msg:
            results.append(pf.determine_which_rule(tup, key_mat, 5, decrypt))
        self.assertSequenceEqual(rule_3, util.list_tuples_to_str(results, True))
        results.clear()

        msg_ints = util.char_to_int_li(rule_2_golden)
        padded_msg = pf.detect_double(msg_ints)
        for tup in padded_msg:
            results.append(pf.determine_which_rule(tup, key_mat, 5, decrypt))
        self.assertSequenceEqual(rule_2, util.list_tuples_to_str(results, True))

def test_rule1(self):
    # Only called when input has same letter in a row
    # Assumes empty strings etc are handled upstream
    golden_a = (23, 23)
    golden_b = (0, 23)
    first_msg = util.char_to_int("X")
    second_msg = util.char_to_int("A")

    first_mod = pf.rule_one(first_msg)
    second_mod = pf.rule_one(second_msg)
    self.assertEqual(len(first_mod), 2)
    self.assertEqual(golden_a, first_mod)

    self.assertEqual(len(second_mod), 2)
    self.assertEqual(golden_b, second_mod)


# def test_rule2(self):
#
# def test_rule3(self):
#
# def test_rule4(self):
#
def test_key_matrix(self):
    golden_matrix = np.array([[2, 17, 8, 19, 4],
                              [0, 1, 3, 5, 6],
                              [7, 10, 11, 12, 13],
                              [14, 15, 16, 18, 20],
                              [21, 22, 23, 24, 25]], dtype=int)
    test_matrix = pf.create_key_matrix(5, util.char_to_int_li("CRITER"))
    self.assertTrue(np.array_equal(golden_matrix, test_matrix), True)
