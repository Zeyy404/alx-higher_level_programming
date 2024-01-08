#!/use/bin/python3
"""Contain a function that adds a new attribute to an object if possible"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Raises a TypeError exception if the object can't have a new attribute.
    """
    if hasattr(obj, "__dict__") or \
       (hasattr(type(obj), "__slots__") and \
        attr_name in type(obj).__slots__):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
