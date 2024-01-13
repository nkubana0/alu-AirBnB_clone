#!/usr/bin/python3
"""Place module"""
from models.base_model import BaseModel

class Place(BaseModel):
    """Place class"""
    def __init__(self, *args, **kwargs):
        """Initialization method"""
        super().__init__(*args, **kwargs)
