# this will be for commonly used functions.
def char_to_int(msg: str) -> list[int]:
    return [ord(s) for s in msg]


def int_to_char(msg: list[int]) -> str:
    return ''.join([chr(s) for s in msg])
