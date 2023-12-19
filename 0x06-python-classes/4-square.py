#!/usr/bin/python3
"""Define a class Square."""

class Square:

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.

        Returns:
            None
        """
        self.__size = size

    def area(self):
        """Returns: the current area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Getter of __size

        Returns:
           the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of __size

        Args:
            value (int): The size of size of the square.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
