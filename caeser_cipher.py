#!/usr/bin/env python

from sys import stdin

CAESER_SHIFT = -3


def main():
    if stdin.isatty():
        cipher_text = input("Cipher text: ")
        print(f"Plain text: {transform_text(cipher_text)}")
    else:
        print(transform_text(input()))


def transform_text(cipher_text):
    return ''.join(transform_character(c) for c in cipher_text.lower())


def transform_character(char):
    # lower case letters are encoded in ASCII starting at 97
    char_num = ord(char) - 97

    # ignore anything that isn't a letter
    if char_num < 0 or char_num > 25:
        return char

    char_num = (char_num + CAESER_SHIFT) % 26
    return chr(char_num + 97)


if __name__ == '__main__':
    main()
