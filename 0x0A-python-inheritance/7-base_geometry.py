#!/usr/bin/python3
"""
Contains BaseGeometry class
"""


class BaseGeometry:
    """Defines BaseGeometry class"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a method that validates value

        Args:
            name (str): a string that contains the name variable
            value (int): an integer that contains the value variable
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
