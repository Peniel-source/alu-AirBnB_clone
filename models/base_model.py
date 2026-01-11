#!/usr/bin/python3
"""Defines the BaseModel class"""
import uuid
from datetime import datetime
import models   # Import the models module, not storage directly


class BaseModel:
    """Base class for all AirBnB clone classes"""

    def __init__(self, *args, **kwargs):
        """Initialization logic"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            import models
            models.storage.new(self)

    def save(self):
        """Updates updated_at and saves to storage"""
        self.updated_at = datetime.now()
        models.storage.save()  # Use models.storage

    def to_dict(self):
        """Returns dictionary representation"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
