#!/usr/bin/python3
"""
Integer validator
"""


class BaseGeometry:
    """
    add public instance method:
            def integer_validator(self, name, value):
    """
    def area(self):
        """
        function: area
        :return:
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function: integer_validator(self, name, value)
        :param name:
        :param value:
        :return:
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
