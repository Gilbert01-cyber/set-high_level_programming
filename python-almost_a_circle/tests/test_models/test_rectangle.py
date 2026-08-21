#!/usr/bin/python3
"""Unittest module for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_width_height(self):
        """Test width and height are set correctly."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_default_x_y(self):
        """Test x and y default to 0."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_custom_x_y(self):
        """Test x and y are set correctly when given."""
        r = Rectangle(10, 2, 1, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 3)

    def test_id_inherited(self):
        """Test id is properly passed to Base."""
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_is_base_instance(self):
        """Test Rectangle instance is also a Base instance."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Rectangle)
        from models.base import Base
        self.assertIsInstance(r, Base)

    def test_width_setter(self):
        """Test the width setter works."""
        r = Rectangle(10, 2)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_height_setter(self):
        """Test the height setter works."""
        r = Rectangle(10, 2)
        r.height = 5
        self.assertEqual(r.height, 5)

    def test_x_setter(self):
        """Test the x setter works."""
        r = Rectangle(10, 2)
        r.x = 5
        self.assertEqual(r.x, 5)

    def test_y_setter(self):
        """Test the y setter works."""
        r = Rectangle(10, 2)
        r.y = 5
        self.assertEqual(r.y, 5)


if __name__ == "__main__":
    unittest.main()
