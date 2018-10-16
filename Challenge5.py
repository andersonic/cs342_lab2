import codecs

def repeating_key_XOR(s, k):
    """Use repeating key XOR, otherwise known as the Vingenere Cipher,
    to encipher a string based on a key."""

    # Convert both message and key to bytes
    str_bytes = bytes(s, encoding='ascii')
    key_bytes = bytes(k, encoding='ascii')

    cipher_bytes = bytearray()

    # XOR each byte in the message with the appropriate byte from the key
    for i in range(len(str_bytes)):
        c = str_bytes[i] ^ key_bytes[i%len(key_bytes)]
        cipher_bytes.append(c)

    # Convert to a hex string and return
    cipher_bytes = bytes(cipher_bytes)
    return codecs.encode(cipher_bytes, 'hex').decode()


if __name__ == "__main__":
    s = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    k = "ICE"

    print(repeating_key_XOR(s, k))