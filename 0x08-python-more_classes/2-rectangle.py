#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:

    """Represent a Rectangle"""
    def __init__(self, width=0, height=0):
        """initialize a Rectangle
        Args:
            width: the width of the Rectangle
            height: the height of the Rectangle

        Returns:
            None
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter of the __width

        Returns:
            the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of the __width

        Args:
           value (int): the value of the width of the Rectangle

        Returns:
           None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter of the __height

        Returns:
            the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of the __height

        Args:
           value (int): the value of the height of the Rectangle

        Returns:
           None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns: the area of the Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns: the perimeter of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
