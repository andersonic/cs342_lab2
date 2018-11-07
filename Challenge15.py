class InvalidPaddingException(Exception):
    pass


def padding_valid(b, size=16):
    if len(b) % size != 0:
        return False
    padding_byte = b[len(b) - 1]
    if not 0 < padding_byte <= size:
        return False
    for i in range(0, padding_byte):
        if b[len(b) - 1 - i] != padding_byte:
            return False
    return True


def remove_padding(b, size=16):
    if not padding_valid(b, size):
        raise InvalidPaddingException
    padding_byte = b[len(b) - 1]
    return b[:len(b) - padding_byte]


if __name__ == "__main__":
    b = b"ICE ICE BABY\x04\x04\x04\x04"
    c = b"ICE ICE BABY\x05\x05\x05\x05"
    d = b"ICE ICE BABY\x01\x02\x03\x04"
    print(padding_valid(b))
    print(padding_valid(c))
    print(padding_valid(d))