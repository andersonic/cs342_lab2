import os, codecs, random
import Challenge10 as c10
import Challenge15 as c15

key = os.urandom(16)


def first_function():
    with open("17.txt", "r") as file:
        strings = file.read().split("\n")

    s = codecs.decode(strings[random.randint(0, len(strings) - 1)].encode(encoding='ascii'), encoding='base64')
    print(s)

    IV = os.urandom(16)

    return c10.encrypt_AES_CBC(s, key, IV), IV


def second_function(c, IV):
    s = c10.aux_decrypt_AES_CBC(c, key, IV)
    return c15.padding_valid(s)


def aux_extract_message(encrypted_block_before_target, target):
    XOR_bytes = bytearray(encrypted_block_before_target)

    temp = [0 for i in range(16)]
    message_so_far = [0 for i in range(16)]

    for j in range(15, -1, -1):
        for i in range(0, 256):
            XOR_bytes[j] = i
            if second_function(target, XOR_bytes):
                temp[j] = i ^ (16 - j)
                message_so_far[j] = i ^ (16-j) ^ encrypted_block_before_target[j]

                for k in range(15, j-1, -1):
                    XOR_bytes[k] = temp[k] ^ (16 - j + 1)
                break

    return bytearray(message_so_far)


def extract_message(c, IV):
    prev_block = IV

    message = bytearray([])

    for i in range(0, len(c), 16):
        current_block = c[i : i + 16]
        message += aux_extract_message(prev_block, current_block)
        prev_block = current_block

    return bytes(message)


if __name__ == "__main__":
    c, IV = first_function()
    print(extract_message(c, IV))