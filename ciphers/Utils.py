# this will be for commonly used functions.
def char_to_int(msg: str) -> list:
    return [ord(s)-65 for s in msg]


def int_to_char(msg: list) -> str:
    return ''.join([chr(s+65) for s in msg])
