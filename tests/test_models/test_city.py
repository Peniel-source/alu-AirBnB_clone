#!/usr/bin/python3
"""
Unit tests for City class.
"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test cases for City class.
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
        Test that City inherits from BaseModel.
        """
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city, City)

    def test_attributes(self):
        """
        Test State City attributes.
        """
        city = City()
        self.assertEqual(city.name, "")

    def test_str(self):
        """
        Test string representation of City.
        """
        city = City()
        string = str(city)
        self.assertIn("[City]", string)
        self.assertIn(city.id, string)


if __name__ == '__main__':
    unittest.main()
