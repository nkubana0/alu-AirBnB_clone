#!/usr/bin/python3
"""
This module contains the State class (Blueprint for creating State objects).
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    This is the state class

    Attributes:
        name (str): The name of the state
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.name = State.name
