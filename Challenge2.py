import codecs


str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"


def fixed_XOR(s1, s2):
    """XOR two same-length strings"""

    # Convert the two strings to bytes
    b1 = codecs.decode(s1, 'hex')
    b2 = codecs.decode(s2, 'hex')

    # XOR each byte and append to a list
    l = []
    for i in range(len(b1)):
        byte = (b1[i] ^ b2[i]).to_bytes(1, 'little')
        t = int.from_bytes(byte, byteorder='little')
        l.append(t)

    # Convert the list back to a hex string
    r = bytes(l)
    return codecs.encode(r, 'hex').decode()


if __name__ == "__main__":
    print(fixed_XOR(str1, str2))