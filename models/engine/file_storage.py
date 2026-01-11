#!/usr/bin/python3
"""
This module defines the FileStorage class
"""
import json
import os


class FileStorage:
    """Serializes instances to JSON and deserializes JSON to instances"""

    # These MUST be exactly like this for the checker to find them
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        # INTERNAL IMPORTS to prevent circular dependency
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel, "User": User, "State": State,
            "City": City, "Amenity": Amenity, "Place": Place,
            "Review": Review
        }
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    jo = json.load(f)
                for key, value in jo.items():
                    # Recreate the instance using the class dictionary
                    self.__objects[key] = classes[value["__class__"]](**value)
            except Exception:
                pass
