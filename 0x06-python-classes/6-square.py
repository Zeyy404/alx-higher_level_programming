#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): the position of the new square

        Returns:
            None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter of the __position

        Returns:
           the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of the __position

        Args:
           value (int, int): the position of the new square

        Returns:
           None
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns: the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #

        Returns:
           None
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(0, min(self.__position[1], self.__size)):
                print("")
            for i in range(0, self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
