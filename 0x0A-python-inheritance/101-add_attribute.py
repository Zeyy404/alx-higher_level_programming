#!/use/bin/python3
"""Contains a function that adds a new attribute to an object if possible"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Raises a TypeError exception if the object can't have a new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
