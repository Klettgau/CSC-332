import numpy as np
import ciphers.Utils as util

# constants
X = 23
i_reduction = 8
j_reduction = 9
alphabet_size = 26
matrix_dim = 5


def encode(msg):
    msg = util.char_to_int(msg)
    key_matrix = create_key_matrix(matrix_dim, [0, 6, 9, 15, 14, 21])

    bigrams = zip(*[msg[i:] for i in range(2)])
    for pair in bigrams:
        print(determine_which_rule(pair, key_matrix, matrix_dim))
    return -1


def decode(msg, _key_matrix):
    return -1


def determine_which_rule(bigram, matrix, dimension):
    # check for same row values, cols, length then else into square
    # So rule one + 2 or 3 or 4 is valid
    first, second = bigram
    print(first,second)
    rows, cols = np.where(matrix == first)
    sec_rows, sec_cols = np.where(matrix == second)
    if len(bigram) < 2 or first == second:
        bigram = rule_one(first)
    if rows[0] == sec_rows[0]:
        bigram = rule_two(matrix, dimension, rows, cols, sec_rows, sec_cols)
        return bigram
    if cols[0] == sec_cols[0]:
        bigram = rule_three(matrix, dimension, rows, cols, sec_rows, sec_cols)
        return bigram
    if rows[0] != sec_rows[0]:
        bigram = rule_four(matrix, dimension, rows, cols, sec_rows, sec_cols)
        return bigram


def rule_one(first_char):
    # check for repeated characaters or one
    result = list()
    result.append(first_char)
    result.append(X)
    return result


def rule_two(matrix, dimension, rows, cols, sec_rows, sec_cols):
    # same row, take right neighbor wrap around
    result = list()
    first_sub = matrix[(rows[0]) % dimension, (cols[0] + 1) % dimension]
    second_sub = matrix[(sec_rows[0]) % dimension, (sec_cols[0] + 1) % dimension]
    result.append(first_sub)
    result.append(second_sub)
    return result


def rule_three(matrix, dimension, rows, cols, sec_rows, sec_cols):
    # column rule, take neighnor below you
    result = list()
    second_sub = matrix[(sec_rows[0] + 1) % dimension, (sec_cols[0]) % dimension]
    first_sub = matrix[(rows[0] + 1) % dimension, (cols) % dimension]
    result.append(first_sub)
    result.append(second_sub)
    return result


def rule_four(matrix, dimension, rows, cols, sec_rows, sec_cols):
    # this is the opposite squre rule,swap y values
    result = list()
    first_sub = matrix[(rows[0]) % dimension, (sec_cols[0]) % dimension]
    second_sub = matrix[(sec_rows[0]) % dimension, (cols[0]) % dimension]
    result.append(first_sub)
    result.append(second_sub)
    return result


def create_key_matrix(dimension: int, seed: list) -> np.ndarray:
    key_mat = np.random.randint(0, 25, (dimension, dimension))
    repeated_char = set()
    row_pos = 0
    pos = 0
    for val in seed:
        if val not in repeated_char:
            col_pos = pos % dimension
            if val == j_reduction or val == i_reduction:
                repeated_char.add(j_reduction)
                repeated_char.add(i_reduction)
            else:
                repeated_char.add(val)
            key_mat[row_pos, col_pos] = val
            if col_pos == dimension - 1:
                row_pos += 1
            pos += 1
    # since I and J are the paired together, subtract one from the count of the add characters.
    if j_reduction in repeated_char or i_reduction in repeated_char:
        col_pos = (len(repeated_char) - 1) % dimension
    else:
        col_pos = (len(repeated_char)) % dimension
    # add the remaining chars in the alphabet
    for num in range(26):
        if num not in repeated_char:
            key_mat[row_pos, col_pos] = num
            if col_pos == dimension - 1:
                row_pos += 1
            col_pos = (col_pos + 1) % dimension

    return key_mat
    # this adds the unique characters in the message to the matrix, need to add the remainder of chars


encode("HELZ")
