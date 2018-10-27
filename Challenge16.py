import Challenge10 as c10
import Challenge2 as c2
import os


key = os.urandom(16)
IV = os.urandom(16)


def first_function(input):
    s = "comment1=cooking%20MCs;userdata=" + \
        input.replace(";", "';'").replace("=", "'='") + \
        ";comment2=%20like%20a%20pound%20of%20bacon"
    return c10.encrypt_AES_CBC(s.encode(encoding='ascii'), key, IV)


def second_function(ciphertext):
    s = c10.decrypt_AES_CBC(ciphertext, key, IV)
    return b";admin=true;" in s


if __name__ == "__main__":
    # first string is length 32
    # second string is length 42
    # admin = true is length 12

    # ; is 59 which is 0011 1011
    # = is 61 which is 0011 1101

    # could write 0011 1111, which is ?

    # figure out which bits to flip to get the ; and = and ; back
    # try bit 5
    # xor with 0000 0100

    # 0000 0010

    c = bytearray(first_function("?admin?true?"))

    b1 = b'\x04'
    b2 = b'\x02'

    first_semicolon = c2.fixed_XOR(b1, bytes([c[16]]))
    equals_sign = c2.fixed_XOR(b2, bytes([c[22]]))
    second_semicolon = c2.fixed_XOR(b1, bytes([c[27]]))

    c[16] = first_semicolon[0]
    c[22] = equals_sign[0]
    c[27] = second_semicolon[0]


    print(second_function(bytes(c)))

