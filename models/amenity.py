#!/usr/bin/python3
"""
This module defines the Amenity class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.
    
    Attributes:
        name (str): Name of the amenity
    """

    name = ""