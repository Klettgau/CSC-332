import numpy as np

# both letters are same or only one is left ,add an X
# 2if both letters are in the same row, replace with neighbor to the right
# 3 if letters are in the same column,replace with neighbor to the right
# 4 opposite corners of the rectange rule, the first letter in message in plaintext is the first ojne to convert
# constants
i_reduction = 8
j_reduction = 9
alphabet_size = 26


def encode(msg, key_matrix):
    return -1


def decode(msg, _key_matrix):
    return -1


def rule_one(bigram):
    # check for repeated characaters or one
    if len(bigram) < 2:
        bigram = "".join(bigram + "x")
        return bigram
    if bigram[0] == bigram[1]:
        bigram = "".join(bigram[0] + "X")
        return bigram


def rule_two(bigram, matrix, dimension):
    # same row, take right neighbor wrap around
    rows, cols = np.where(matrix == bigram[0])
    sec_rows, sec_cols = np.where(matrix == bigram[1])

    first_sub = matrix[(rows[0]) % dimension, (cols[0] + 1) % dimension]
    second_sub = matrix[(sec_rows[0]) % dimension, (sec_cols[0] + 1) % dimension]
    return "".join(first_sub + second_sub)


def rule_three(bigram, matrix, dimension):
    # column rule, take neighnor below you
    rows, cols = np.where(matrix == bigram[0])
    sec_rows, sec_cols = np.where(matrix == bigram[1])
    second_sub = matrix[(sec_rows[0] + 1) % dimension, (sec_cols[0]) % dimension]
    first_sub = matrix[(rows[0] + 1) % dimension, (cols) % dimension]

    return "".join(first_sub + second_sub)

def rule_four(bigram, matrix, dimension):
    # this is the opposite squre rule
    return -1


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


create_key_matrix(5, list(dict.fromkeys([5, 9, 6, 7, 8, 10, 1, 11, 1])))
