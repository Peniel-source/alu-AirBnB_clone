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
        Deserialize the JSON file to __objects (only if the JSON file exists).
        If the file doesn't exist, do nothing and no exception should be raised.
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                
            for key, value in obj_dict.items():
                class_name = value['__class__']
                # Import classes dynamically to avoid circular imports
                if class_name == 'BaseModel':
                    from models.base_model import BaseModel
                    cls = BaseModel
                elif class_name == 'User':
                    from models.user import User
                    cls = User
                elif class_name == 'State':
                    from models.state import State
                    cls = State
                elif class_name == 'City':
                    from models.city import City
                    cls = City
                elif class_name == 'Amenity':
                    from models.amenity import Amenity
                    cls = Amenity
                elif class_name == 'Place':
                    from models.place import Place
                    cls = Place
                elif class_name == 'Review':
                    from models.review import Review
                    cls = Review
                else:
                    continue
                    
                FileStorage.__objects[key] = cls(**value)
                
        except FileNotFoundError:
            pass