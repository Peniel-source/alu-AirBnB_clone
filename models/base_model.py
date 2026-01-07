#!/usr/bin/python3
"""
This module defines the BaseModel class which serves as the base class
for all other classes in the AirBnB clone project.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods for other classes.
    
    Attributes:
        id (str): Unique identifier for each instance
        created_at (datetime): Timestamp when instance is created
        updated_at (datetime): Timestamp when instance is last updated
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        
        Args:
            *args: Variable length argument list (not used)
            **kwargs: Arbitrary keyword arguments for creating instance from dict
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Return string representation of BaseModel instance.
        
        Returns:
            str: String in format [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Update the updated_at attribute with current datetime and save to storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Return dictionary representation of BaseModel instance.
        
        Returns:
            dict: Dictionary containing all keys/values of __dict__ plus __class__
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict