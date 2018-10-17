import Challenge2 as c2
import codecs, sys, string


str_to_decipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


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


def decipher_single_XOR(b):
    """Given a message that has been XOR'd with a single character,
        return the message."""
    strings = []

    for i in range(0, 128):
        c = bytearray()
        for j in range(len(b)):
            c.append(i)

        temp = c2.fixed_XOR(b, bytes(c))

        if temp: strings.append((temp, i))
    return pick_english(strings)


def aux_decipher_single_XOR(s):
    message = codecs.decode(s, 'hex')
    return decipher_single_XOR(message)


if __name__ == "__main__":
    message, key = aux_decipher_single_XOR(str_to_decipher)
    print("Message: " + codecs.decode(message))
    print("Key: " + chr(key))