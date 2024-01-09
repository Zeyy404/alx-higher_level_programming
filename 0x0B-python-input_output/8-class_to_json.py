#!/usr/bin/python3
"""This module defines a class-to-JSON function"""
import json


def class_to_json(obj):
    """Converts an object to a dictionary suitable for JSON serialization.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representing the object's attributes and their values.
    """
    return obj.__dict__
