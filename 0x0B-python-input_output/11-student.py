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
        if type(attrs) == list and \
           all(type(elem) == str for elem in attrs):
            for attr in attrs:
                if hasattr(self, attr):
                    return {attr: getattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all public attributes of the Student instance with values
              from a JSON dictionary.

        Args:
            json (dict): A dictionary containing attribute names as keys
               and their corresponding values.
        """
        for key, value in json.items():
            setattr(self, key, value)
