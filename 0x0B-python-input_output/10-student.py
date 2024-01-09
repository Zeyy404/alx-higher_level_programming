#!/usr/bin/python3
"""This module defines the Student class"""


class Student:
    """Defines the Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize the Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance.

        Args:
           attrs (list of strings): List of attribute names to include
                If None, all attributes are included. Defaults to None.

        Returns:
           Dictionary containing the specified attributes and their values
        """
        if (type(attrs) == list and
            all(type(elem) == str for elem in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
