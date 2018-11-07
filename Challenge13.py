import os
import Challenge10 as c10

uid = 0
key = os.urandom(16)


def encipher_profile(profile):
    return c10.encrypt_AES_ECB(profile, key)


def decipher_profile(profile):
    return c10.decrypt_AES_ECB(profile, key)


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
    return s


if __name__ == "__main__":
    s = profile_for("mail@gmail.com").encode(encoding='ascii')
    a = encipher_profile("'admin'".encode(encoding='ascii'))
    c = encipher_profile(s)

    a_p = decipher_profile(c[0:32] + a).decode()
    print(parse(a_p))