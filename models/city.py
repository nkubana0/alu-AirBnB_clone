#!/usr/bin/python3
"""
This module contains the City class (Blueprint for creating City objects).
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    This is the city class

    Attributes:
        state_id (str): The state id
        name (str): The name of the city
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
