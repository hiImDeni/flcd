from math import floor


def get_ascii(symbol):
    if not isinstance(symbol, str):
        return None
    asciiSum = 0
    for char in symbol:
        asciiSum += ord(char)
    return asciiSum


def hash_code(size, symbol, tries):
    key = 0
    if isinstance(symbol, int):
        key = abs(symbol)
    elif isinstance(symbol, float):
        key = abs(floor(symbol))
    elif isinstance(symbol, str):
        key = get_ascii(symbol)

    return int(key % size + 0.5 * tries + 0.5 * tries * tries)