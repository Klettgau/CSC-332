# this will be for commonly used functions.
import itertools
def char_to_int_li(msg: str) -> list:
    return [ord(s)-65 for s in msg]

def char_to_int(msg:str)->int:
    return ord(msg.upper())-65

def list_to_str(msg):
    return ''.join(msg)

def list_tuples_to_str(msg:list,strinFlag=False)->str:
    if strinFlag:
        return int_to_char(list(itertools.chain.from_iterable(msg)))
    return ''.join(list(itertools.chain.from_iterable(msg)))


def int_to_char(msg: list) -> str:
    return ''.join([chr(s+65) for s in msg])
