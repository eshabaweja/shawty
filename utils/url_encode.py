def to_decimal(input_str):
    to_bytes = bytes(input_str, 'utf-8')
    # directly convert bytes to decimal
    return int.from_bytes(to_bytes, 'big')


def base62_encode(input_str):
    base = 62
    base62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    encoded = ""
    deci = to_decimal(input_str)
    
    while deci > 0:
        remainder = deci % base
        deci //= base
        encoded = base62[remainder] + encoded

    return encoded
    