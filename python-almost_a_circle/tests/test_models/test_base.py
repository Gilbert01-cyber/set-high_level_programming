#!/usr/bin/python3
"""Unittest module for the Base class."""
import unittest
from models.base import Base


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

if __name__ == "__main__":
    unittest.main()
