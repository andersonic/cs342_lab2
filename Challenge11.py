import os, random, codecs
import Challenge10 as c10

def generate_AES_key():
    return os.urandom(16)


def encryption_oracle(s):
    s = os.urandom(random.randint(5, 10)) + s + os.urandom(random.randint(5, 10))
    k = generate_AES_key()
    cbc = random.randint(0,1)
    if cbc:
        IV = generate_AES_key()
        return c10.encrypt_AES_CBC(s, k, IV), cbc
    else:
        return c10.encrypt_AES_ECB(s, k), cbc


def detect_block_cipher_used(ciphertext):
    d = {}
    for i in range(0, len(ciphertext), 16):
        enciphered_block = ciphertext[i: i + 16]
        if enciphered_block in d:
            d[enciphered_block] += 1
        else:
            d[enciphered_block] = 1
    # Determine how many repeated blocks there are
    current_score = 0
    for key in d:
        current_score += d[key] - 1
    return current_score


if __name__ == '__main__':
    with open('11.txt', 'r') as file:
        s = file.read().encode('ascii', 'ignore')
    #s = codecs.decode(s, 'base64')

    """d = [[0,0],[0,0]]

    for i in range(0, 1000):
        c = encryption_oracle(s)
        cbc = c[1]
        n = detect_block_cipher_used(c[0])
        if n: n = 1
        else: n = 0
        d[cbc][n] += 1
    print(d)"""

    c = encryption_oracle(s)
    cbc = not (detect_block_cipher_used(c[0]))
    if cbc: print("CBC")
    else: print("EBC")