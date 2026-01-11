#!/usr/bin/python3
"""
Unit tests for User class.
"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test cases for User class.
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
        Test that User inherits from BaseModel.
        """
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertIsInstance(user, User)

    def test_attributes(self):
        """
        Test User class attributes.
        """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_str(self):
        """
        Test string representation of User.
        """
        user = User()
        string = str(user)
        self.assertIn("[User]", string)
        self.assertIn(user.id, string)


if __name__ == '__main__':
    unittest.main()
