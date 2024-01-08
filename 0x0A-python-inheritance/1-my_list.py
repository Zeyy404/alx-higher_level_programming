#!/usr/bin/python3
"""
Contains MyList class definition
"""


class MyList(list):
    """a subclass of the class list"""

    def __init__(self):
        """initializing the subclass"""

        super().__init__()

    def print_sorted(self):
        """Prints the list, but sorted(ascending sort)"""

        print(sorted(self))
