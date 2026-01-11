#!/usr/bin/python3
"""
This module initializes the models package and creates a storage instance.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
