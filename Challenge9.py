import codecs


def pad_text(text_to_pad, length):
    assert len(text_to_pad) <= length
    padding_amount = length - len(text_to_pad)
    padding = bytearray([padding_amount for i in range(padding_amount)])
    padded_text = bytes(bytearray(text_to_pad, encoding='ascii') + padding)
    return padded_text


if __name__ == "__main__":
    print(pad_text("YELLOW SUBMARINE", 20))