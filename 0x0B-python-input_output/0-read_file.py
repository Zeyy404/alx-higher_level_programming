#!/usr/bin/python3
"""This module defines a text file-reading funtion"""


def read_file(filename=""):
    """Print the content of UTF8 file to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
