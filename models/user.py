#!/usr/bin/python3
"""User module"""
from models.base_model import BaseModel

class User(BaseModel):
    """User class"""
    def __init__(self, *args, **kwargs):
        """Initialization method"""
        super().__init__(*args, **kwargs)
