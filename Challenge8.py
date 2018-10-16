import codecs


def detect_AES_ECB(ciphertexts):
    max_score = 0
    max_text = None

    for ciphertext in ciphertexts:
        d = {}
        for i in range(0, len(ciphertext), 16):
            enciphered_block = ciphertext[i: i + 16]
            if enciphered_block in d:
                d[enciphered_block] += 1
            else:
                d[enciphered_block] = 1
        current_score = 0
        for key in d:
            current_score += d[key] - 1
        if current_score > max_score:
            max_score = current_score
            max_text = ciphertext

    return max_text


if __name__ == "__main__":
    with open("c8.txt", "r") as file:
        messages = file.read().split("\n")

    messages = [codecs.decode(message.encode('ascii'), 'base64') for message in messages]
    print(detect_AES_ECB(messages))