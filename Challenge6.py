import sys, codecs, string


def hamming_distance(b1, b2):
    """Compute the edit distance/hamming distance of two strings that have
    already been converted to bytes."""
    dist = 0

    # Compute whether each bit of each byte is the same or not
    for i in range(len(b1)):
        t = b1[i] ^ b2[i]
        for j in range(8):
            if 1 & t:
                dist += 1
            t >>= 1
    return dist


def get_keysize(s):
    """Given a message that has been enciphered with repeated-key XOR,
    return the most likely key size, defined by the keysize with the
    lowest normalized hamming distance between blocks of keysize-sized
    text."""

    current_size = 0
    current_score = sys.maxsize

    # Compute the normalized hamming distsance between
    # keysize-sized blocks of text for all keysizes
    # between 2 and 40.
    for keysize in range(2, 40):
        s1 = s[0:keysize]
        s2 = s[keysize: 2 * keysize]
        s3 = s[keysize * 2: keysize*3]
        s4 = s[keysize * 3: keysize * 4]
        dist1 = hamming_distance(s1, s2)
        dist2 = hamming_distance(s1, s3)
        dist3 = hamming_distance(s1, s4)
        dist4 = hamming_distance(s2, s3)
        dist5 = hamming_distance(s2, s4)
        dist6 = hamming_distance(s3, s4)
        ave_dist = (dist1 + dist2 + dist3 + dist4 + dist5 + dist6)/(3 * keysize)
        if ave_dist < current_score:
            current_score = ave_dist
            current_size = keysize
    return current_size


def english_score(b):
    """Rate how English-like a piece of text is, based on letter frequency."""
    count = 0
    for c in b:
        c = chr(c)
        if c == 'e' or c == 't' or c == 'a' or c == 'o' or c == 'i' or c == 'n':
            count += 2
        elif c == 's' or c == 'r' or c == 'h' or c =='l' or c == 'd' or c =='c':
            count += 1
        elif c == 'f' or c == 'p' or c =='g' or c == 'w' or c =='y' or c =='b':
            count -= 1
        elif c == 'v' or c == 'k' or c == 'x' or c == 'j' or c == 'q' or c == 'z':
            count -= 2
        elif c not in string.printable:
            count -= 10
    return count


def pick_english(l):
    """Given a list of strings, return the one that is most English-like
    in letter frequency."""
    strings = [item[0] for item in l]
    current_score = - sys.maxsize - 1
    current_str = None
    current_chr = None

    for i in range(len(strings)):
        score = english_score(strings[i])
        if score > current_score:
            current_str = strings[i]
            current_score = score
            current_chr = l[i][1]

    return current_str, current_chr


def fixed_XOR(b1, b2):
    """XOR two same-length strings"""
    l = []
    for i in range(len(b1)):
        byte = (b1[i] ^ b2[i]).to_bytes(1, 'little')
        t = int.from_bytes(byte, byteorder='little')
        l.append(t)
    r = bytes(l)
    return r


def decipher_single_XOR(b):
    """Given a message that has been XOR'd with a single character,
        return the message."""
    strings = []

    for i in range(0, 128):
        c = bytearray()
        for j in range(len(b)):
            c.append(ord(chr(i)))

        temp = fixed_XOR(b, bytes(c))

        if temp: strings.append((temp, i))
    return pick_english(strings)


def break_repeating_key_XOR(s):
    """Given a ciphertext that has been enciphered
    with repeating key XOR, find the key"""

    # Determine the keysize
    keysize = get_keysize(s)

    # Create a bytearray for each letter in the key
    blocks = [bytearray() for i in range(keysize)]
    for i in range(len(s)):
        blocks[i % keysize].append(s[i])

    # Determine what the key is, block by block
    key = ""
    for block in blocks:
        key += chr(decipher_single_XOR(bytes(block))[1])

    return key


def decipher_repeating_key_XOR(ciphertext, key):
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
        m.append(fixed_XOR(blocks[i], bytes(c)))

    # Piece the message back together
    message = ""
    for i in range(len(ciphertext)):
        message += chr(m[i % len(m)][i // len(m)])
    return message


if __name__ == "__main__":
    with open("6.txt", "r") as file:
        text = file.read().encode('ascii')
    t = codecs.decode(text, 'base64')

    # Find the key
    key = break_repeating_key_XOR(t)

    print(decipher_repeating_key_XOR(t, key))