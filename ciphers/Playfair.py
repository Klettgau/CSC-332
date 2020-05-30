import numpy as np
import ciphers.Utils as util
import itertools
# constants
X = 23
i_reduction = 8
j_reduction = 9
alphabet_size = 26
matrix_dim = 5


def encode_decode(msg,decrypt,key_matrix=None):
    msg = util.char_to_int(msg)
    msg = pad_message(msg)
    if key_matrix is None:
        key_matrix = create_key_matrix(matrix_dim, [0, 6, 9, 15, 14, 21])
    print(key_matrix)
    bigrams = detect_double(msg)
    return util.int_to_char(itertools.chain.from_iterable(list(map(lambda x:determine_which_rule(x,key_matrix,matrix_dim,decrypt),bigrams))))

def determine_which_rule(bigram, matrix, dimension,decrypt=False):
    # check for same row values, cols, length then else into square
    # So rule one + 2 or 3 or 4 is valid
    first, second = bigram
    rows, cols = np.where(matrix == first)
    sec_rows, sec_cols = np.where(matrix == second)
    if rows[0] == sec_rows[0]:
        first_char,second_char = rule_two(matrix, dimension, rows, cols, sec_rows, sec_cols,decrypt)
        return first_char,second_char
    if cols[0] == sec_cols[0]:
        first_char,second_char= rule_three(matrix, dimension, rows, cols, sec_rows, sec_cols,decrypt)
        return first_char,second_char
    if rows[0] != sec_rows[0]:
        first_char,second_char = rule_four(matrix, dimension, rows, cols, sec_rows, sec_cols)
        return first_char,second_char


def pad_message(msg):
    if len(msg) < 2:
        msg.append(X)
    if len(msg) % 2 != 0:
        msg.append(X)
    return msg


def detect_double(msg):
    bigrams = [(msg[i], msg[i + 1]) for i in range(0, len(msg), 2)]
    updated_bigram = list()
    for x,y in bigrams:
        if   x == y:
            x_first,x_second = rule_one(x)
            y_first,y_second=rule_one(y)
            updated_bigram.append((x_first,x_second))
            updated_bigram.append((y_first,y_second))
        else:
            updated_bigram.append((x,y))
    return updated_bigram
def rule_one(first_char):
    # check for repeated characaters or one
    return first_char,X


def rule_two(matrix, dimension, rows, cols, sec_rows, sec_cols,decrypt=False):
    # same row, take right neighbor wrap around
    if decrypt:
        first_sub = matrix[(rows[0]) % dimension, (cols[0] - 1) % dimension]
        second_sub = matrix[(sec_rows[0]) % dimension, (sec_cols[0] - 1) % dimension]
    else:
        first_sub = matrix[(rows[0]) % dimension, (cols[0] + 1) % dimension]
        second_sub = matrix[(sec_rows[0]) % dimension, (sec_cols[0] + 1) % dimension]
    return first_sub,second_sub


def rule_three(matrix, dimension, rows, cols, sec_rows, sec_cols,decrypt=False):
    # column rule, take neighnor below you
    if decrypt:
        second_sub = matrix[(sec_rows[0] -1) % dimension, (sec_cols[0]) % dimension]
        first_sub = matrix[(rows[0] -1) % dimension, (cols) % dimension]
    else:
        second_sub = matrix[(sec_rows[0] + 1) % dimension, (sec_cols[0]) % dimension]
        first_sub = matrix[(rows[0] + 1) % dimension, (cols) % dimension]
    return first_sub,second_sub


def rule_four(matrix, dimension, rows, cols, sec_rows, sec_cols):
    # this is the opposite squre rule,swap y values
    first_sub = matrix[(rows[0]) % dimension, (sec_cols[0]) % dimension]
    second_sub = matrix[(sec_rows[0]) % dimension, (cols[0]) % dimension]
    return first_sub,second_sub


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

print(util.char_to_int("PLEASESENDHELP"))
res=encode_decode("PLEASESENDHELPP",False)
print(res)
print(util.char_to_int(res))
print(encode_decode(res,True))
