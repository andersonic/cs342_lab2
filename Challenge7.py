import codecs
from Crypto.Cipher import AES


def decrypt_AES_ECB(s, k):
    """Given ciphertext that has been enciphered using AES
    in ECB mode and a key, recover the plaintext message."""
    cipher = AES.new(k, AES.MODE_ECB)
    return codecs.decode(cipher.decrypt(s))


if __name__ == "__main__":
    with open("c7.txt", "r") as file:
        ciphertext = file.read().encode('ascii')
    key = "YELLOW SUBMARINE"

    # Convert the message to bytes
    s = codecs.decode(ciphertext, 'base64')

    # Ensure that the key is also of type bytes
    k = codecs.encode(key, 'ascii')

    # Get message and print it
    print(decrypt_AES_ECB(s, k))
