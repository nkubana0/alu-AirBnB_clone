#!/usr/bin/python3

from models.base_model import BaseModel

class State(BaseModel):
    """State class."""
    def __init__(self, name="", **kwargs):
        super().__init__(**kwargs)
        self.name = name

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a State instance from a dictionary."""
        state_instance = cls(**obj_dict)
        return state_instance
