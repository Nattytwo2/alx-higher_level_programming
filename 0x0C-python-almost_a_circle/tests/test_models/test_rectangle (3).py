#!/usr/bin/python3
"""Unittest for Rectangle module"""
import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    This is the class unittest for the max integer function
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_Rectangle_class(self):
        R = Rectangle(1, 1)
        self.assertIsInstance(R, Rectangle)

    def test_Rectangle_id(self):
        R = Rectangle(1, 1)
        r = Rectangle(2, 2)
        self.assertEqual(r.id, 2)

    def test_Rectangle_id_increase(self):
        R = Rectangle(1, 1)
        r = Rectangle(2, 2)
        r1 = Rectangle(3, 3)
        self.assertEqual(r1.id, 3)

    def test_Rectangle_id2(self):
        r1 = Rectangle(4, 4, id=12)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 4)

    def test_subclass_rectangle(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_Rectangle_width_error(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)

    def test_Rectangle_height_error(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "2")

    def test_Rectangle_x_error(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(4, 4, -2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 4, "2")

    def test_Rectangle_y_error(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(4, 4, 2, -2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(4, 4, 2, "2")

    def test_area_Rectangle(self):
        r = Rectangle(4, 4)
        self.assertEqual(r.area(), 16)
        r1 = Rectangle(12, 2, 8, 1, 1)
        self.assertEqual(r1.area(), 24)

    def test_update1_Rectangle(self):
        r = Rectangle(1, 1)
        r.update(89, 2, 2, 2, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 89)

    def test_update2_Rectangle(self):
        r = Rectangle(1, 1)
        r.update(x=2, y=3, id=4, width=5, height=6)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 4)

    def test_to_dictionary_Rectangle(self):
        r = Rectangle(89, 1, 1, 1, 1)
        self.assertEqual(dict, type(r.to_dictionary()))

    def test_display_Rectangle(self):
        r = Rectangle(1, 1)
        draw = "#\n"
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r.display()
        self.assertEqual(f.getvalue(), draw)
        r1 = Rectangle(3, 2)
        draw = "###\n###\n"
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), draw)


if __name__ == '__main__':
    unittest.main()
