import Challenge3 as c3
import codecs

filename = ''


if __name__ == "__main__":
    with open('4.txt', 'r') as file:
        ciphertexts = file.read().split("\n")

    # Convert text to ascii
    ciphertexts = [text.encode('ascii') for text in ciphertexts]

    # Create a list to hold potential messages
    potential_messages = []

    # Get the most likely message from each ciphertext
    for text in ciphertexts:
        temp = c3.decipher_single_XOR(text)
        if temp: potential_messages.append(temp)

    # Pick the message that is most likely to be English
    message, key = c3.pick_english(potential_messages)
    print("Message: " + codecs.decode(message))
    print("Key: " + chr(key))
