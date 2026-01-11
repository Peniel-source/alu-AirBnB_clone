#!/usr/bin/python3
"""
This module defines the City class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.

    Attributes:
        state_id (str): State ID (will be State.id)
        name (str): Name of the city
    """

    state_id = ""
    name = ""
