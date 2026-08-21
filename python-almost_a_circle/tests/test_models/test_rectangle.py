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

    def test_width_not_int(self):
        """Test TypeError raised when width is not an int."""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_width_str(self):
        """Test TypeError raised when width is a string."""
        with self.assertRaises(TypeError) as e:
            Rectangle("10", 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_width_negative(self):
        """Test ValueError raised when width is negative."""
        with self.assertRaises(ValueError) as e:
            Rectangle(-10, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_width_zero(self):
        """Test ValueError raised when width is zero."""
        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_height_negative(self):
        """Test ValueError raised when height is negative."""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, -2)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_height_zero(self):
        """Test ValueError raised when height is zero."""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 0)
        self.assertEqual(str(e.exception), "height must be > 0")

    def test_x_not_int(self):
        """Test TypeError raised when x is not an int."""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_x_negative(self):
        """Test ValueError raised when x is negative."""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, -3)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_y_not_int(self):
        """Test TypeError raised when y is not an int."""
        with self.assertRaises(TypeError) as e:
            Rectangle(10, 2, 0, "1")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_y_negative(self):
        """Test ValueError raised when y is negative."""
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_width_setter_negative(self):
        """Test ValueError raised when width setter gets negative."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError) as e:
            r.width = -10
        self.assertEqual(str(e.exception), "width must be > 0")


    def test_area(self):
        """Test the area method."""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_display(self):
        """Test the display method output without offset."""
        import io
        import sys
        r1 = Rectangle(2, 3)
        captured = io.StringIO()
        sys.stdout = captured
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n" * 3)

    def test_display_with_offset(self):
        """Test the display method output with x/y offset."""
        import io
        import sys
        r1 = Rectangle(2, 3, 2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        r1.display()
        sys.stdout = sys.__stdout__
        expected = "\n\n" + "  ##\n" * 3
        self.assertEqual(captured.getvalue(), expected)

    def test_str(self):
        """Test the __str__ method output."""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1, 0, 9)
        self.assertEqual(str(r2), "[Rectangle] (9) 1/0 - 5/5")

if __name__ == "__main__":
    unittest.main()
