import numpy as np

table = {0: 'A', 1: 'D', 2: 'F', 3: 'G', 4: 'V', 5: 'X'}

def seed_polybius(seed):
    '''
    This method creates the Polybius table for the encoding/decoding.
    :param seed: A string to prime the secret alphabet.
    :return: A numpy 6x6 array of a-z 0-9
    '''
    encountered = set()
    poly = np.random.permutation(36).reshape((6, 6))
    row = 0
    for pos, c in enumerate(seed):
        mod_val = pos % 6
        if pos > 0 and mod_val is 0:
            row += 1
        if c in encountered:
            break
        else:
            encountered.add(c)
            rez = np.where(poly == (ord(c) - 97))
            tmp = poly[row, mod_val]
            poly[row, mod_val] = ord(c) - 97
            poly[rez[0], rez[1]] = tmp
    return poly


def convert_using_key(secret_msg, polybius):
    '''
    The method takes the message e.g "the" and produces ['AF', 'VG', 'FX'].
    :param secret_msg: The message to be communicated.
    :param polybius: The Polybius table/secret alphabet.
    :return: Numpy array of the message converted according to the Table.
    '''
    # step 1 after priming the secret alphabet
    encoded = list()
    for pos, c in enumerate(secret_msg):
        res = np.where(polybius == (ord(c) - 97))
        encoded.append(table[res[0][0]] + table[res[1][0]])
    return np.array(encoded).reshape((len(secret_msg) // 4, 4))


def sort_private_key(secret_key):
    '''
    Produces the order in which the matrix columns need to be organized
    according to the secret key.
    :param secret_key: The predetermined key to encode the message.
    :return: A list of tuples [('i',1),('i',3)]
    '''
    headers = list()
    for pos, c in enumerate(secret_key):
        headers.append((c, pos))
    order = sorted(headers)
    print(order)
    return order


def columnar_transpostion(secret_key, adfgvx_mat):
    '''
    Produces the encoded array by arranging columns.
    :param secret_key: The predetermined key to encode the message.
    :param adfgvx_mat: The matrix of the form AV GD CV
    :return: The final encoded array which is sent to the party.
    '''
    # step 2  after creating the matrix
    order = sort_private_key(secret_key)
    encoded_matrix_sorted = list()
    for _, x in order:
        encoded_matrix_sorted.append([adfgvx_mat[y, x] for y in range(4)])
    return np.array(encoded_matrix_sorted)


def secret_table_lookup(dec, secret_alph, lookup):
    '''

    :param dec:
    :param secret_alph:
    :param lookup:
    :return:
    '''
    print(dec)
    coords = list()
    for x in range(4):
        for y in range(4):
            coords.append(tuple((str(dec[x, y])[2], str(dec[x, y])[3])))
    msg = list()
    for pair in coords:
        x = lookup[pair[0]]
        y = lookup[pair[1]]
        msg.append(chr(secret_alph[x, y] + 97))
    return ''.join(msg)


def encode_message(secret_key, secret_msg, poly):
    k = convert_using_key(secret_msg, poly)
    print(k, " convert")
    # repeat letters when sorted will be undetermined
    encoded_sorted_matrix = columnar_transpostion(secret_key, k)
    return encoded_sorted_matrix


def decode_message(secret_key, encoded_msg_mat, secret_alph):
    '''
    :param secret_key: The key used in the columnar transposition.
    :param encoded_msg_mat: The encoded matrix in a numpy array.
    :param secret_alph: The polybius table used.
    :return: A string representation of the message.
    '''
    order = sort_private_key(secret_key)
    msg_matrix_columnar_reversed = np.zeros((4, 4), dtype="S3", )

    for i, count in reversed(list(enumerate(order))):
        print(i, count)
        _,pos = count
        msg_matrix_columnar_reversed[:, pos] = encoded_msg_mat[i, :]
    # for count in range(len(order) - 1, -1, -1):
    #     _, pos = order[count]
    #     msg_matrix_columnar_reversed[:, pos] = encoded_msg_mat[count, :]
    lookup = dict([(v, k) for (k, v) in table.items()])
    print(msg_matrix_columnar_reversed, " reversed")
    return secret_table_lookup(msg_matrix_columnar_reversed, secret_alph, lookup)


# row then column for values

msg_seed = "thebangles"
msg_key = "riki"
secret_msg = "iliketomoveititt"
matrix = seed_polybius(msg_seed)
print(matrix, "seeded polybius")
encoded_msg = encode_message(msg_key, secret_msg, matrix)
print(encoded_msg, " encoded msg")
print(decode_message(msg_key, encoded_msg, matrix))
