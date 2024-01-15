#!/usr/bin/python3
"""Contains the Square class definition that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initailize the Square class"""
        super().__init__(size, size, x, y)

    def __str__(self):
        """Returns: string representation of the Square attributes"""
        string = '[' + str(self.__class__.__name__) + '] '
        string += '(' + str(self.id) + ') '
        string += str(self._Rectangle__x) + '/' + str(self._Rectangle__y)
        string += ' - ' + str(self._Rectangle__width)
        return string

    @property
    def size(self):
        """Getter of the Square size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of the size attribute of the Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns: the dictionary representation of a Square"""
        return {
            'id': self.id,
            'x': self._Rectangle__x,
            'size': self.width,
            'y': self._Rectangle__y
        }
