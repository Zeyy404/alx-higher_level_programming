#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    """Represent a Rectangle"""
    def __init__(self, width=0, height=0):
        """initialize a Rectangle
        Args:
            width: the width of the Rectangle
            height: the height of the Rectangle

        Returns:
            None
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Returns: string representation of the Rectangle (#)"""

        result = ""
        for _ in range(self.__height):
            result += str(self.print_symbol) * self.__width + '\n'
        return result.rstrip()

    def __repr__(self):
        """Returns: a string representation of the Rectangle for recreation"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two instances of Rectangle based on the area

        Args:
           rect_1: 1st instance of Rectangle
           rect_2: 2nd instance of Rectangle

        Returns: the biggest Recatangle based on area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns: a new Rectangle instance with width == height == size

        Args:
           size: the size of the new Rectangle (square)
        """
        return cls(size, size)
