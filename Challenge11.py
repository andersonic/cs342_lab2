import os, random, codecs
import Challenge10 as c10

def generate_AES_key():
    return os.urandom(16)


def encryption_oracle(s):
    s = os.urandom(random.randint(5, 10)) + s + os.urandom(random.randint(5, 10))
    k = generate_AES_key()
    ecb = random.randint(0,1)
    if ecb:
        return c10.encrypt_AES_ECB(s, k), ecb
    else:
        IV = generate_AES_key()
        return c10.encrypt_AES_CBC(s, k, IV), ecb


def detect_ebc(chosen_ciphertext):
    return chosen_ciphertext[16:32] == chosen_ciphertext[32:48]


if __name__ == '__main__':
    s = bytes([0 for i in range(43)])
    c = encryption_oracle(s)

    ecb = detect_ebc(c[0])

    if c[1]: print("Ground truth: ECB")
    else: print("Ground truth: CBC")

    if ecb:print("Detected: ECB")
    else: print("Detected: CBC")