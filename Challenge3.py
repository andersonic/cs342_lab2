import Challenge2 as c2
import codecs, sys, string


str_to_decipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


def english_score(s):
    """Rate how English-like a piece of text is, based on letter frequency"""
    s = s.lower()

    count = 0
    for c in s:
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


def pick_english(strings):
    """Given a list of strings, return the one that is most English-like
    in letter frequency."""
    current_score = - sys.maxsize - 1
    current_str = None

    for i in range(len(strings)):
        score = english_score(strings[i])
        if score > current_score:
            current_str = strings[i]
            current_score = score

    return current_str


def hexstr_to_str(hexstr):
    """Given a hex string, convert to a text string"""
    temp = codecs.decode(hexstr, 'hex')
    try:
        return temp.decode('ascii')
    except UnicodeDecodeError:
        return None


def decipher_single_XOR(s):
    """Given a message that has been XOR'd with a single character,
    return the message."""

    # Create a list to hold potential messages
    strings = []

    # Loop through all possible characters and determine the message if that
    # character were the key
    for i in range(0, 127):
        b = bytearray()
        for j in range(len(s)):
            b.append(i)
        XOR_str = codecs.encode(b, 'hex').decode()

        temp = codecs.encode(c2.fixed_XOR(s, XOR_str))
        temp = hexstr_to_str(temp)

        if temp: strings.append(temp)

    # Pick the potential message that is most English-like in letter
    # frequency
    return pick_english(strings)


if __name__ == "__main__":
    print(decipher_single_XOR(str_to_decipher))