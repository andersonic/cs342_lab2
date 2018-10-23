import codecs
from Crypto.Cipher import AES
import Challenge2 as c2


def aux_encrypt_AES_ECB(s, k):
    cipher = AES.new(k, AES.MODE_ECB)
    return cipher.encrypt(s)


def encrypt_AES_ECB(s, k):
    return aux_decrypt_AES_ECB(pad_to_16(s), k)


def aux_decrypt_AES_ECB(s,k):
    cipher = AES.new(k, AES.MODE_ECB)
    return cipher.decrypt(s)

def decrypt_AES_ECB(s, k):
    return unpad(aux_decrypt_AES_ECB(s,k))


def pad_to_16(b):
    padding_length = 16 - (len(b) % 16)
    padding = bytearray([padding_length for i in range(padding_length)])
    return bytes(b + padding)


def unpad(b):
    padding = b[len(b) - 1]
    return b[:len(b) - padding]


def aux_encrypt_AES_CBC(s, k, IV):
    previous_block_encypted = IV
    encrypted_message = bytearray()
    for i in range(0, len(s), 16):
        block = s[i: i + 16]
        block_to_encrypt = c2.fixed_XOR(block, previous_block_encypted)
        encrypted_block = aux_encrypt_AES_ECB(block_to_encrypt, k)
        encrypted_message += encrypted_block
        previous_block_encypted = encrypted_block
    return bytes(encrypted_message)

def encrypt_AES_CBC(s, k, IV):
    s = pad_to_16(s)
    return aux_encrypt_AES_CBC(s, k, IV)


def aux_decrypt_AES_CBC(s, k, IV):
    decrypted_message = bytearray()

    previous_decrypted_block = None
    for i in range(len(s) - 16, -1, -16):
        block = s[i: i + 16]
        if previous_decrypted_block:
            decrypted_message = c2.fixed_XOR(previous_decrypted_block, block) + decrypted_message
        previous_decrypted_block = aux_decrypt_AES_ECB(block, k)
    decrypted_message = c2.fixed_XOR(previous_decrypted_block, IV) + decrypted_message
    return bytes(decrypted_message)


def decrypt_AES_CBC(s, k, IV):
    return unpad(aux_decrypt_AES_CBC(s, k, IV))


if __name__ == "__main__":
    IV = bytes([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    with open('10.txt', 'r') as file:
        s = file.read().encode(encoding='ascii')
    s = codecs.decode(s, 'base64')
    k = codecs.encode("YELLOW SUBMARINE", encoding='ascii')
    print(decrypt_AES_CBC(s, k, IV).decode())
