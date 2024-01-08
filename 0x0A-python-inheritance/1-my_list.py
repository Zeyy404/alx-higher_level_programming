#!/usr/bin/python3
"""
Contains MyList class definition that inherits from the list
"""


class MyList(list):
    """a subclass of the class list"""

    def print_sorted(self):
        """Prints the list sorted(ascending sort)"""
        print(sorted(self))
