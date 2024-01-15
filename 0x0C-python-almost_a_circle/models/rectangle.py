#!/usr/bin/python3
"""Contains the definition of Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Definition of the Recatangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter of the __x attribute

        Returns:
           the x value of the recatangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of the __x

        Args:
           value (int): the value of the x of the Rectangle

        Returns:
           None
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter of the __y attribute

        Returns:
           the y value of the recatangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of the __y

        Args:
           value (int): the value of the y of the Rectangle

        Returns:
           None
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        """Returns: the area value of the of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for _ in range(self.__height):
            for j in range(self.__x):
                print(' ', end='')
            print('#' * self.__width)

    def __str__(self):
        """Returns: string represenation of the Rectangle attributes"""
        string = '[' + str(self.__class__.__name__) + '] '
        string += '(' + str(self.id) + ') '
        string += str(self.__x) + '/' + str(self.__y)
        string += ' - ' + str(self.__width) + '/' + str(self.__height)
        return string

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns: the dictionary representation of a Rectangle"""
        return {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
        }
