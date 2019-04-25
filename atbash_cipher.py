#!/usr/bin/env python

from sys import stdin

from ciphers.atbash import transform_text


def main():
    if stdin.isatty():
        cipher_text = input("Cipher text: ")
        print(f"Plain text: {transform_text(cipher_text)}")
    else:
        print(transform_text(input()))


if __name__ == '__main__':
    main()
