#!/usr/bin/python3
"""
Base Model

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update method"""
        if args and len(args) != 0:
            i = 0
            att_list = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, att_list[i], args[i])
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """to_dictionary method"""
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y, }
