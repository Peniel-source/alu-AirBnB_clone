#!/usr/bin/python3
"""
Unit tests for FileStorage class.
"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage class.
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

    def test_all(self):
        """
        Test all method of FileStorage.
        """
        storage = FileStorage()
        objects = storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        """
        Test new method of FileStorage.
        """
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, storage.all())

    def test_save_reload(self):
        """
        Test save and reload methods of FileStorage.
        """
        storage = FileStorage()
        model = BaseModel()
        model.name = "Test Model"
        storage.new(model)
        storage.save()

        # Check if file was created
        self.assertTrue(os.path.exists("file.json"))

        # Create new storage and reload
        new_storage = FileStorage()
        new_storage.reload()
        key = "BaseModel.{}".format(model.id)
        self.assertIn(key, new_storage.all())

        # Check if attributes are preserved
        reloaded_model = new_storage.all()[key]
        self.assertEqual(reloaded_model.name, "Test Model")
        self.assertEqual(reloaded_model.id, model.id)


if __name__ == '__main__':
    unittest.main()