#!/usr/bin/python3
"""Unittest for Base module"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """
    This is the class unittest for the max integer function
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_Base_class(self):
        B = Base()
        self.assertIsInstance(B, Base)

    def test_Base_id(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_Base_id_increase(self):
        b = Base()
        b1 = Base()
        self.assertEqual(b1.id, 2)

    def test_Base_id2(self):
        b = Base()
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_Base_str(self):
        b = Base("Foo")
        self.assertEqual("Foo", b.id)

    def test_subclass_rectangle(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_subclass_square(self):
        self.assertTrue(issubclass(Square, Base))


if __name__ == '__main__':
    unittest.main()
