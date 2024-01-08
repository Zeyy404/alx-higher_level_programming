#!/usr/bin/python3
"""Contains MyInt class"""


class MyInt(int):
    def __eq__(self, other):
        """Invert the behavior of =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the behavior of !="""
        return super().__eq__(other)
