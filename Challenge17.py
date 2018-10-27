import os, codecs, random
import Challenge10 as c10
import Challenge15 as c15


key = os.urandom(16)


def first_function():
    with open("17.txt", "r") as file:
        strings = file.read().split("\n")

    s = codecs.decode(strings[random.randint(0, len(strings) - 1)].encode(encoding='ascii'), encoding='base64')

    IV = os.urandom(16)

    return c10.encrypt_AES_CBC(s, key, IV), IV


def second_function(c, IV):
    s = c10.aux_decrypt_AES_CBC(c, key, IV)
    return c15.padding_valid(s)


if __name__ == "__main__":
    c, IV = first_function()
    print(second_function(c, IV))