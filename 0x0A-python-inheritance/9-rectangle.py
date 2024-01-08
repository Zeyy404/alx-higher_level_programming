#!/usr/bin/python3
"""Contains Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle class"""

    def __init__(self, width, height):
        """initialize Rectangle class"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns: the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns: print() and str() represenation of the Rectangle"""
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return string
