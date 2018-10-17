import codecs
import Challenge2 as c2

def repeating_key_XOR(str_bytes, key_bytes):
    """Use repeating key XOR, otherwise known as the Vingenere Cipher,
    to encipher a string based on a key."""

    cipher_bytes = bytearray()

    # XOR each byte in the message with the appropriate byte from the key
    for i in range(len(str_bytes)):
        c = str_bytes[i] ^ key_bytes[i%len(key_bytes)]
        cipher_bytes.append(c)

    # Convert to a hex string and return
    cipher_bytes = bytes(cipher_bytes)
    return cipher_bytes


def repeating_key_XOR1(ciphertext, key):
    """Given a message that has been enciphered using key and
    repeating key XOR, return the original message."""

    # Make blocks of ciphertext for each letter of the key
    blocks = [bytearray() for i in range(len(key))]
    for i in range(len(ciphertext)):
        blocks[i % len(key)].append(ciphertext[i])
    m = []

    # Decipher each block of ciphertext
    for i in range(len(blocks)):
        c = bytearray()
        for j in range(len(blocks[i])):
            c.append(ord(key[i]))
        m.append(c2.fixed_XOR(blocks[i], bytes(c)))

    # Piece the message back together
    message = ""
    for i in range(len(ciphertext)):
        message += chr(m[i % len(m)][i // len(m)])
    return message



if __name__ == "__main__":
    s = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal"
    k = "ICE"


    temp = repeating_key_XOR(bytes(s, encoding='ascii'), bytes(k, encoding='ascii'))

    print(codecs.encode(temp, 'hex').decode())