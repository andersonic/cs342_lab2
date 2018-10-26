import Challenge10 as c10
import os


key = os.urandom(16)
IV = os.urandom(16)


def first_function(input):
    s = "comment1=cooking%20MCs;userdata=" + \
        input.replace(";", "';'").replace("=", "'='") + \
        ";comment2=%20like%20a%20pound%20of%20bacon"
    return c10.encrypt_AES_CBC(s.encode(encoding='ascii'), key, IV)



def second_function(ciphertext):
    s = c10.decrypt_AES_CBC(ciphertext, key, IV)
    return ";admin=true;" in s.decode()

if __name__ == "__main__":
    print(second_function(first_function(";admin=true;")))