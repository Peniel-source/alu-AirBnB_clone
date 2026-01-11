#!/usr/bin/python3
"""
Unit tests for Place class.
"""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test cases for Place class.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        pass

    def tearDown(self):
        """
        Clean up test environment.
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_inheritance(self):
        """
        Test that Place inherits from BaseModel.
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        """
        Test Place class attributes.
        """
        place = Place()
        self.assertEqual(place.name, "")

    def test_str(self):
        """
        Test string representation of Place.
        """
        place = Place()
        string = str(place)
        self.assertIn("[Place]", string)
        self.assertIn(place.id, string)


if __name__ == '__main__':
    unittest.main()
