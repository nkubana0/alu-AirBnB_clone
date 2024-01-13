#!/usr/bin/python3
"""City module"""
from models.base_model import BaseModel

class City(BaseModel):
    """City class"""
    def __init__(self, *args, **kwargs):
        """Initialization method"""
        super().__init__(*args, **kwargs)
