# this will be for commonly used functions.
def char_to_int_li(msg: str) -> list:
    return [ord(s)-65 for s in msg]

def char_to_int(msg:str)->int:
    return ord(msg.upper())-65

def list_to_str(msg):
    return ''.join(msg)


def int_to_char(msg: list) -> str:
    return ''.join([chr(s+65) for s in msg])
