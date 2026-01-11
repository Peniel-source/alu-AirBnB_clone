#!/usr/bin/python3
"""
This module defines the FileStorage class that handles serialization
and deserialization of instances to/from JSON file.
"""
import json
import os


class FileStorage:
    """
    FileStorage class that serializes instances to JSON file and
    deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to the JSON file
        __objects (dict): Dictionary to store all objects by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects.

        Returns:
            dict: Dictionary containing all stored objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id.

        Args:
            obj: Object to be stored
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path).
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'State': State,
            'City': City, 'Amenity': Amenity, 'Place': Place,
            'Review': Review
        }

        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name in classes:
                        cls = classes[class_name]
                        FileStorage.__objects[key] = cls(**value)
            except Exception:
                pass
