#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
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

    def test_init(self):
        """
        Test BaseModel initialization.
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """
        Test string representation of BaseModel.
        """
        model = BaseModel()
        string = str(model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(model.id, string)

    def test_save(self):
        """
        Test save method of BaseModel.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """
        Test to_dict method of BaseModel.
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_init_from_dict(self):
        """
        Test BaseModel initialization from dictionary.
        """
        model = BaseModel()
        model.name = "Test Model"
        model.number = 42
        model_dict = model.to_dict()

        new_model = BaseModel(**model_dict)
        self.assertEqual(model.id, new_model.id)
        self.assertEqual(model.created_at, new_model.created_at)
        self.assertEqual(model.updated_at, new_model.updated_at)
        self.assertEqual(model.name, new_model.name)
        self.assertEqual(model.number, new_model.number)
        self.assertIsNot(model, new_model)


if __name__ == '__main__':
    unittest.main()
