#!/usr/bin/python3
"""
Unit tests for State class.
"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for State class.
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
        Test that State inherits from BaseModel.
        """
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state, State)

    def test_attributes(self):
        """
        Test State class attributes.
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_str(self):
        """
        Test string representation of State.
        """
        state = State()
        string = str(state)
        self.assertIn("[State]", string)
        self.assertIn(state.id, string)


if __name__ == '__main__':
    unittest.main()
