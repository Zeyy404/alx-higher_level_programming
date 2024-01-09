#!/usr/bin/python3
"""This module defines a file append-writing function"""


def append_write(filename="", text=""):
    """Appends a string at the end of a UTF8 text file

    Returns:
       the number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
