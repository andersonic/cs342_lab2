import Challenge10 as c10
import Challenge12 as c12
import os, random


padding_size = (5,10)


def encryption_oracle(input):

    b = os.urandom(random.randint(padding_size[0], padding_size[1]))

    s = b + input + c12.unknown_string
    return c10.encrypt_AES_ECB(s, c12.key)


def using_ECB(f, blocksize):
    i = bytes([0 for i in range(blocksize * 2 + blocksize-padding_size[0])])
    c = f(i)
    return c[blocksize:2*blocksize] == c[2*blocksize:3*blocksize]


def find_blocksize(f):
    pass



if __name__ == "__main__":
    print(using_ECB(encryption_oracle, 16))