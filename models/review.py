#!/usr/bin/python3
"""Review module"""
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class"""
    def __init__(self, *args, **kwargs):
        """Initialization method"""
        super().__init__(*args, **kwargs)
