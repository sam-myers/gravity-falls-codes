#!/usr/bin/env python

from sys import stdin

from ciphers.caeser import transform_text

CAESER_SHIFT = -3


def main():
    if stdin.isatty():
        cipher_text = input("Cipher text: ")
        print(f"Plain text: {transform_text(cipher_text, CAESER_SHIFT)}")
    else:
        print(transform_text(input(), CAESER_SHIFT))


if __name__ == '__main__':
    main()
