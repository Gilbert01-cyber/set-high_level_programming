#!/usr/bin/python3
"""Unittest module for the Square class."""
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def test_size(self):
        """Test that size sets both width and height."""
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_default_x_y(self):
        """Test x and y default to 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_custom_x_y(self):
        """Test x and y are set correctly when given."""
        s = Square(3, 1, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_id(self):
        """Test id is properly passed to Base."""
        s = Square(5, 0, 0, 12)
        self.assertEqual(s.id, 12)

    def test_is_rectangle_instance(self):
        """Test Square instance is also a Rectangle instance."""
        s = Square(5)
        self.assertIsInstance(s, Square)
        self.assertIsInstance(s, Rectangle)

    def test_area(self):
        """Test the area method for a Square."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Test the __str__ method output."""
        s1 = Square(5, 0, 0, 1)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s2 = Square(2, 2, 0, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")

    def test_size_not_int(self):
        """Test TypeError raised when size is not an int."""
        with self.assertRaises(TypeError) as e:
            Square("5")
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_size_negative(self):
        """Test ValueError raised when size is negative."""
        with self.assertRaises(ValueError) as e:
            Square(-5)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_size_zero(self):
        """Test ValueError raised when size is zero."""
        with self.assertRaises(ValueError) as e:
            Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")


    def test_size_getter(self):
        """Test the size getter."""
        s1 = Square(5)
        self.assertEqual(s1.size, 5)

    def test_size_setter(self):
        """Test the size setter updates width and height."""
        s1 = Square(5)
        s1.size = 10
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(str(s1), "[Square] ({}) 0/0 - 10".format(s1.id))

    def test_size_setter_not_int(self):
        """Test TypeError raised when size setter gets a non-int."""
        s1 = Square(5)
        with self.assertRaises(TypeError) as e:
            s1.size = "9"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_size_setter_negative(self):
        """Test ValueError raised when size setter gets negative."""
        s1 = Square(5)
        with self.assertRaises(ValueError) as e:
            s1.size = -1
        self.assertEqual(str(e.exception), "width must be > 0")

if __name__ == "__main__":
    unittest.main()
