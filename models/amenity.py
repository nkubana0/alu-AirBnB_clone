#!/usr/bin/python3
"""Amenity module"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class"""
    def __init__(self, *args, **kwargs):
        """Initialization method"""
        super().__init__(*args, **kwargs)
