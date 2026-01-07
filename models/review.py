#!/usr/bin/python3
"""
This module defines the Review class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.
    
    Attributes:
        place_id (str): Place ID (will be Place.id)
        user_id (str): User ID (will be User.id)
        text (str): Review text
    """

    place_id = ""
    user_id = ""
    text = ""