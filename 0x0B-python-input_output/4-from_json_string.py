#!/usr/bin/python3
"""This module defines an JSON-to-obj function"""
import json


def from_json_string(my_str):
    """Returns: an object(Python data structure) represented by JSON string"""
    return json.loads(my_str)
