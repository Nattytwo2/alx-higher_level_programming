#!/usr/bin/python3
"""
Real definition of a rectangle

"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """The __init__ method of the square class
        Args:
            width(int): Private attribute default 0
            height(int): Private attribute default 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Private instance attribute getter method."""
        return self.__width

    @property
    def height(self):
        """Private instance attribute getter method."""
        return self.__height

    @width.setter
    def width(self, value):
        """Private instance attribute property setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Private instance attribute property setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Measure area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Measure perimeter."""
        if not (self.__width == 0 or self.__height == 0):
            return ((self.__width + self.__height) * 2)
        return 0

    def __str__(self):
        """String conversion"""
        if self.width == 0 or self.height == 0:
            return ("")
        rectangle = ((('#' * self.__width) + '\n') * self.__height)[:-1]
        return rectangle
