#!/usr/bin/python3
"""This module defines a file-writing using JASON function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
