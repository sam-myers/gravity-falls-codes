def transform_text(cipher_text, shift):
    return ''.join(transform_character(c, shift) for c in cipher_text.lower())


def transform_character(char, shift):
    # lower case letters are encoded in ASCII starting at 97
    char_num = ord(char) - 97

    # ignore anything that isn't a letter
    if char_num < 0 or char_num > 25:
        return char

    char_num = (char_num + shift) % 26
    return chr(char_num + 97)
