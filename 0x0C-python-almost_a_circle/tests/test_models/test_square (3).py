#!/usr/bin/python3
"""Unittest for Square module"""
import unittest
import io
import contextlib
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    This is the class unittest for the max integer function
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_Square_class(self):
        R = Square(1)
        self.assertIsInstance(R, Square)

    def test_Square_id(self):
        R = Square(1)
        r = Square(2)
        self.assertEqual(r.id, 2)

    def test_Square_id_increase(self):
        R = Square(1)
        r = Square(2)
        r1 = Square(3)
        self.assertEqual(r1.id, 3)

    def test_Square_id2(self):
        r1 = Square(4, id=12)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.size, 4)

    def test_subclass_Square(self):
        self.assertTrue(issubclass(Square, Base))

    def test_Square_size_error(self):
        with self.assertRaises(ValueError):
            r1 = Square(-1)
        with self.assertRaises(TypeError):
            r1 = Square("1")

    def test_Square_x_error(self):
        with self.assertRaises(ValueError):
            r1 = Square(4, -2)
        with self.assertRaises(TypeError):
            r1 = Square(4, "2")

    def test_Square_y_error(self):
        with self.assertRaises(ValueError):
            r1 = Square(4, 2, -2)
        with self.assertRaises(TypeError):
            r1 = Square(4, 2, "2")

    def test_area_Square(self):
        r = Square(4)
        self.assertEqual(r.area(), 16)
        r1 = Square(12, 2, 1, 1)
        self.assertEqual(r1.area(), 144)

    def test_update1_Square(self):
        r = Square(1)
        r.update(89, 2, 2, 2)
        self.assertEqual(r.size, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 89)

    def test_update2_Square(self):
        r = Square(1, 1)
        r.update(x=2, y=3, id=4, size=5)
        self.assertEqual(r.size, 5)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 4)

    def test_to_dictionary_Square(self):
        r = Square(89, 1, 1, 1)
        self.assertEqual(dict, type(r.to_dictionary()))

    def test_display_Square(self):
        r = Square(1)
        draw = "#\n"
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), draw)
        r1 = Square(2)
        draw = "##\n##\n"
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), draw)


if __name__ == '__main__':
    unittest.main()
