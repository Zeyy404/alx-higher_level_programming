#!/usr/bin/python3
"""This module defines an object from a JSON file creating function"""
import json


def load_from_json_file(filename):
    """Creates an Object from a "JSON file\""""
    with open(filename) as f:
        return json.load(f)
