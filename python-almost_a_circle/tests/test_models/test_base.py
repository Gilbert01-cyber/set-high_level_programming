#!/usr/bin/python3
"""Unittest module for the Base class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_id_public(self):
        """Test that id is a public attribute."""
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_no_id_first(self):
        """Test that first instance without id gets id 1."""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_no_id_increment(self):
        """Test that ids auto-increment for instances without id."""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_given_id_no_increment(self):
        """Test that passing an id doesn't affect the counter."""
        Base._Base__nb_objects = 0
        b1 = Base(89)
        b2 = Base()
        self.assertEqual(b1.id, 89)
        self.assertEqual(b2.id, 1)


    def test_to_json_string_none(self):
        """Test to_json_string with None returns '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list returns '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """Test to_json_string with a list of dictionaries."""
        list_dicts = [{"id": 12}]
        result = Base.to_json_string(list_dicts)
        self.assertEqual(result, '[{"id": 12}]')

    def test_to_json_string_type(self):
        """Test to_json_string returns a string."""
        result = Base.to_json_string([{"id": 12}])
        self.assertIsInstance(result, str)

    def test_save_to_file_none(self):
        """Test save_to_file with None saves an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test save_to_file with an empty list."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_list(self):
        """Test save_to_file writes correct JSON for a list of objects."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        expected = Rectangle.to_json_string([r1.to_dictionary()])
        self.assertEqual(content, expected)

if __name__ == "__main__":
    unittest.main()
