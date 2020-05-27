import string
import numpy
from flask import jsonify
from flask_restful import Resource


def generate_key( dimension, test_flag):
    counter = 0
    if test_flag == 1:
        return numpy.array([[23, 2, 17, 17],
                            [15, 25, 21, 18],
                            [21, 19, 9, 13],
                            [19, 6, 24, 21]]), numpy.array([[10, 13, 19, 21],
                                                            [21, 14, 5, 10],
                                                            [19, 8, 16, 5],
                                                            [14, 11, 25, 22]])
    while True:
        counter += 1
        key = numpy.random.randint(0, 26, (dimension, dimension))
        inv_key, signal = modinv(key)
        if signal:
            break
    return key, inv_key


def modinv( key):
    det = int(round(numpy.linalg.det(key) % 26))
    dinv = numpy.round((numpy.linalg.det(key) * numpy.linalg.inv(key)))
    number = numpy.arange(1, 27)
    rez = numpy.mod(det * number, 26)
    zz = numpy.where(rez == 1)
    if numpy.size(zz) == 0:
        return (-1, False)
    zz = zz[0].item(0) + 1  # one off
    key_matrix = numpy.mod(zz * dinv, 26).astype(int)  # the adjuate * d^-1
    # key inverse K-1
    return (key_matrix, True)


def pad_message( msg, key_row):
    msg_size = len(msg)
    while msg_size % key_row != 0:
        for i, ele in enumerate(msg):
            msg.append(ele)
            if len(msg) % key_row == 0:
                break
        if len(msg) % key_row == 0:
            break
    return msg


def resize_array( msg, dimension):
    msg_array = numpy.array(msg)
    msg_len = msg_array.shape[0]
    msg_array.resize((int(msg_len / dimension), dimension))
    return msg_array


def encode( msg, dimension, test_flag=0):
    lower_message = [string.ascii_lowercase.index(i) for i in msg]
    padded_message = pad_message(lower_message, dimension)
    key, inv_key = generate_key(dimension, test_flag)
    msg_array = resize_array(padded_message, dimension)
    print(msg_array)
    return numpy.mod(numpy.dot(msg_array, key), 26), inv_key


def decode( encoded_matrix, key):
    return{'decoded_message': numpy.mod(numpy.dot(encoded_matrix, key), 26),
                    'encode_message': encoded_matrix,
                    'key': key}


msg, inv_key = encode("retreat", 4)
print(msg)
print(decode(msg, inv_key))
