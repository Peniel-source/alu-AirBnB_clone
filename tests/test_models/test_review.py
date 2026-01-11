#!/usr/bin/python3
"""
Unit tests for Review class.
"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test cases for Review class.
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
        Test that Review inherits from BaseModel.
        """
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        """
        Test Review class attributes.
        """
        review = Review()
        # Check for the correct attributes defined in models/review.py
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_str(self):
        """
        Test string representation of Review.
        """
        review = Review()
        string = str(review)
        self.assertIn("[Review]", string)
        self.assertIn(review.id, string)


if __name__ == '__main__':
    unittest.main()
