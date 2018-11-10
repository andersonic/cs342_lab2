import Challenge10 as c10
import Challenge12 as c12
import os, random


padding_size = (0, 16)
random_prefix = os.urandom(random.randint(padding_size[0], padding_size[1]))


def encryption_oracle(input):
    s = random_prefix + input + c12.unknown_string
    return c10.encrypt_AES_ECB(s, c12.key)


def get_blocksize(f):
    count = 100
    blocksize = 1
    while True:
        c = f(bytes("a" * count, encoding='ascii'))
        if c[blocksize:blocksize*2] == c[blocksize*2:blocksize*3] == c[blocksize*3:blocksize*4]:
            return blocksize

        blocksize += 1
        if blocksize > count // 4:
            count += 100


def using_ECB(f, blocksize):
    i = bytes([0 for i in range(blocksize * 2 + blocksize-padding_size[0])])
    c = f(i)
    return c[blocksize:2*blocksize] == c[2*blocksize:3*blocksize]


def extract_message(blocksize=16):
    zeros = encryption_oracle(bytearray([0 for i in range(0,blocksize*2)]))[blocksize:blocksize*2]
    known = False
    num_random_bytes = blocksize
    while not known:
        b = encryption_oracle(bytearray([0 for i in range(0, 32 - num_random_bytes)]))
        if b[blocksize:blocksize*2] == zeros:
            break
        num_random_bytes -= 1

    size = len(encryption_oracle(bytearray()))

    current_block = 1
    input_length = blocksize - 1 + blocksize - num_random_bytes
    message = bytearray()

    while len(message) < size:
        input = bytearray("a" * input_length, encoding='ascii')

        block_to_match = encryption_oracle(input)[current_block * blocksize: (current_block + 1) * blocksize]

        input += message

        for i in range(0, 256):
            c = encryption_oracle(input + bytearray([i]))
            if c[current_block * blocksize: (current_block + 1) * blocksize] == block_to_match:
                message.append(i)
                break

        input_length -= 1
        if input_length < 0:
            input_length = blocksize - 1
            current_block += 1

    return message


if __name__ == "__main__":
    if using_ECB(encryption_oracle, 16):
        print(extract_message(get_blocksize(encryption_oracle)).decode(encoding='ascii'))