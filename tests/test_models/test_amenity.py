#!/usr/bin/python3
"""
Unit tests for Amenity class.
"""
import unittest
import os
from models.state import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity class.
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
        Test that Amenity inherits from BaseModel.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        """
        Test Amenity class attributes.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_str(self):
        """
        Test string representation of Amenity.
        """
        amenity = Amenity()
        string = str(amenity)
        self.assertIn("[Amenity]", string)
        self.assertIn(amenity.id, string)


if __name__ == '__main__':
    unittest.main()
