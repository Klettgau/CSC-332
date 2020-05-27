import numpy as np

# both letters are same or only one is left ,add an X
# 2if both letters are in the same row, replace with neighbor to the right
# 3 if letters are in the same column,replace with neighbor to the right
# 4 opposite corners of the rectange rule, the first letter in message in plaintext is the first ojne to convert
# constants
I = 8
J = 9


def encode(msg, key_matrix):
    return -1


def decode(msg, _key_matrix):
    return -1


def create_key_matrix(dimension: int, seed: list) -> np.ndarray:
    key_mat = np.random.randint(0, 25, (dimension, dimension))
    repeated_char = set()
    row_pos = 0
    for pos, val in enumerate(seed):
        if val not in repeated_char:
            col_pos = pos % dimension
            if val == I or val == J:
                repeated_char.add(I)
                repeated_char.add(J)
            else:
                repeated_char.add(val)
            key_mat[row_pos, col_pos] = val
            if col_pos == dimension - 1:
                row_pos += 1
    if I in repeated_char or J in repeated_char:
        col_pos = (len(repeated_char) - 1) % dimension
    else:
        col_pos = (len(repeated_char)) % dimension
    for num in range(25):
        if num not in repeated_char:
            key_mat[row_pos, col_pos] = num
            if col_pos == dimension - 1:
                row_pos += 1
            col_pos = (col_pos + 1) % dimension

    return key_mat
    # this adds the unique characters in the message to the matrix, need to add the remainder of chars


create_key_matrix(5, [5, 6, 7, 8, 10, 11])
