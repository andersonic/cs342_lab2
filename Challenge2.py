import codecs


str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"


def fixed_XOR_hexstr(s1, s2):
    # Convert the two strings to bytes
    b1 = codecs.decode(s1, 'hex')
    b2 = codecs.decode(s2, 'hex')
    return codecs.encode(fixed_XOR(b1, b2), 'hex').decode()


def fixed_XOR(b1, b2):
    """XOR two same-length strings"""

    l = []
    for i in range(len(b1)):
        byte = (b1[i] ^ b2[i]).to_bytes(1, 'little')
        t = int.from_bytes(byte, byteorder='little')
        l.append(t)
    r = bytes(l)
    return r


if __name__ == "__main__":
    print(fixed_XOR_hexstr(str1, str2))