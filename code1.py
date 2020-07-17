#!/usr/bin/env python3
import os
import binascii from cryptography.hazmat.primitives.ciphers
import Cipher , algorithms , modes from cryptography.hazmat.primitives
import padding from cryptography.hazmat.backends import default_backend
import argparse
def readfile_binary(file):
    with open(file , ’rb’) as f:
        content = f.read()
    return content
def writefile_binary(file , content):
    with open(file , ’wb’) as f:
        f.write(content)
def main():
    parser = argparse.ArgumentParser(description = ’Some explanation about this code’)
    parser.add_argument(’-in’, dest = ’input’, required = True)
    parser.add_argument(’-out’, dest = ’output’, required = True)
    parser.add_argument(’-K’, dest = ’key’, help = ’The key to be used for encryption , must be in hex’)
    parser.add_argument(’-iv’, dest = ’iv’, help = ’The Initilisation Vector , must be in hex’)
    args = parser.parse_args()
    input_content = readfile_binary(args.input)
if __name__ == "__main__":
    main()
