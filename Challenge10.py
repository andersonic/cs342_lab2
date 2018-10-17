import codecs
from Crypto.Cipher import AES
import Challenge2 as c2


def encrypt_AES_ECB(s, k):
    cipher = AES.new(k, AES.MODE_ECB)
    return cipher.encrypt(s)


def decrypt_AES_ECB(s, k):
    cipher = AES.new(k, AES.MODE_ECB)
    return cipher.decrypt(s)


def encrypt_AES_CBC(s, k, IV):
    previous_block_encypted = IV
    encrypted_message = bytearray()
    for i in range(0, len(s), 16):
        block = s[i: i + 16]
        block_to_encrypt = c2.fixed_XOR(block, previous_block_encypted)
        encrypted_block = encrypt_AES_ECB(block_to_encrypt, k)
        encrypted_message += encrypted_block
        previous_block_encypted = encrypted_block
    return bytes(encrypted_message)


def decrypt_AES_CBC(s, k, IV):

    decrypted_message = bytearray()
    for i in range(len(s) - 16, -1, -16):
        block = s[i: i + 16]
        decrypted_block = decrypt_AES_ECB(block, k)

if __name__ == "__main__":
    for i in range(256-16, -1, -16):
        print(i)
