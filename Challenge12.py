import os,codecs
import Challenge10 as c10

key = os.urandom(16)
unknown_string = codecs.decode("Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK".encode('ascii'), 'base64')


def encryption_oracle(input):
    s = input + unknown_string
    return c10.encrypt_AES_ECB(s, key)


def find_blocksize():
    count = 1
    prev_block = None
    while count > 0:
        current_block = encryption_oracle(bytes("a" * count, encoding='ascii'))
        if prev_block and current_block[0:count - 1] == prev_block[0:count - 1]:
            return count - 1
        else:
            prev_block = current_block
            count += 1


def using_ECB(f, blocksize):
    i = bytes([0 for i in range(32)])
    c = f(i)
    return c[0:blocksize] == c[blocksize:2* blocksize]


def extract_message(blocksize):
    size = len(encryption_oracle(bytearray()))

    current_block = 0
    input_length = blocksize - 1
    message = bytearray()

    while len(message) < size:
        input = bytearray("a" * input_length, encoding='ascii')

        block_to_match = encryption_oracle(input)[current_block * blocksize: (current_block + 1) * blocksize]

        input += message

        for i in range(0,256):
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
    blocksize = find_blocksize()
    if using_ECB(encryption_oracle, blocksize):
        print(extract_message(blocksize).decode())
    else:
        print("Sorry can't help you.")
