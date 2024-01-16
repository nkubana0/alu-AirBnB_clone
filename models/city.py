#!/usr/bin/python3

from models.base_model import BaseModel

class City(BaseModel):
    """City class."""
    def __init__(self, name="", state_id="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.state_id = state_id

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a City instance from a dictionary."""
        city_instance = cls(**obj_dict)
        return city_instance
