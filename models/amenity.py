#!/usr/bin/python3

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class."""
    def __init__(self, name="", **kwargs):
        super().__init__(**kwargs)
        self.name = name

    @classmethod
    def from_dict(cls, obj_dict):
        """Create an Amenity instance from a dictionary."""
        amenity_instance = cls(**obj_dict)
        return amenity_instance
