import codecs


def detect_AES_ECB(ciphertexts):
    """Given a list of ciphertexts, determine which one has
    been enciphered using AES on ECB mode. Determine this by
    determining which ciphertext has the most repeated blocks."""
    max_score = 0
    max_text = None

    for ciphertext in ciphertexts:
        # Count the number of times each block appears in
        # a given ciphertext
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

        # If this ciphertext has more repeated blocks than
        # the ciphertext with the most repeated blocks seen
        # so far, this ciphertext becomes the one with the
        # most repeated blocks
        if current_score > max_score:
            max_score = current_score
            max_text = ciphertext

    return max_text


if __name__ == "__main__":
    with open("c8.txt", "r") as file:
        messages = file.read().split("\n")

    messages = [codecs.decode(message.encode('ascii'), 'hex') for message in messages]
    print(detect_AES_ECB(messages))