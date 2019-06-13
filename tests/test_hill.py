import unittest
from ciphers import Hill
import string
import numpy


class HillTest(unittest.TestCase):

    def test_encode(self):
        hill = Hill.Hill()
        msg = "generalkenobi"
        dimension = 4
        encoded_msg, inv_key = hill.encode(msg, dimension, test_flag=1)
        correct_encode = numpy.array([[1, 19, 9, 11],
                                      [6, 17, 4, 18],
                                      [2, 7, 23, 11],
                                      [7, 8, 12, 23]])
        numpy.testing.assert_array_equal(encoded_msg, correct_encode)

    def test_resize(self):
        hill = Hill.Hill()
        test_msg = [string.ascii_lowercase.index(i) for i in "boatymcboat"]
        # execute
        corr_msg = numpy.array([[4, 23, 4, 2], [20, 19, 4, 4]])
        test_nar = hill.resize_array(test_msg, 4)
        self.assertEqual(test_nar.shape, corr_msg.shape, "these should be the same tuple.")

    def test_pad_message(self):
        hill = Hill.Hill()
        msg = "kenobi"
        lower_message = [string.ascii_lowercase.index(i) for i in msg]
        padded_msg = hill.pad_message(lower_message, 15)
        self.assertEqual(len(padded_msg), 15)

    def test_modinv(self):
        hill = Hill.Hill()
        key = numpy.array([[23, 2, 17, 17],
                           [15, 25, 21, 18],
                           [21, 19, 9, 13],
                           [19, 6, 24, 21]])
        inv_key_corr = numpy.array([[10, 13, 19, 21],
                                    [21, 14, 5, 10],
                                    [19, 8, 16, 5],
                                    [14, 11, 25, 22]])
        inv_key, signal = hill.modinv(key)
        numpy.testing.assert_array_equal(inv_key, inv_key_corr)
        self.assertTrue(signal, True)


if __name__ == '__main__':
    unittest.main()
