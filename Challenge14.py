import Challenge10 as c10
import Challenge12 as c12
import os, random


def encryption_oracle(input):

    b = os.urandom(random.randint(5, 10))

    s = b + input + c12.unknown_string
    return c10.encrypt_AES_ECB(s, c12.key)


def using_ECB(f):
    i = bytes([0 for i in range(43)])
    c = f(i)
    return c[16:32] == c[32:48]


if __name__ == "__main__":
    print(using_ECB(encryption_oracle))