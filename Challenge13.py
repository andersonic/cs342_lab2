import os

uid = 0


def generate_random_AES_key():
    return os.urandom(16)


def parse(s):
    pieces = s.split("&")
    d = {}
    for piece in pieces:
        assert("=" in piece)
        i = piece.index("=")
        d[piece[:i]] = piece[i+1:]
    return d


def profile_for(email):
    global uid
    email = email.replace("&", "").replace("=", "")
    s = "email=" + email + "&uid=" + str(uid) + "&role='user'"
    uid += 1
    return s


if __name__ == "__main__":
    print(profile_for("test"))
    print(parse(profile_for('test')))