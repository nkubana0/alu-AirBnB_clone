#!/usr/bin/python3

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class."""
    def __init__(self, name="", **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def to_dict(self):
        """Return a dictionary representation of the Amenity instance."""
        amenity_dict = super().to_dict()
        amenity_dict['name'] = self.name
        return amenity_dict

    # Add any additional methods or properties as needed

    @classmethod
    def from_dict(cls, obj_dict):
        """Create an Amenity instance from a dictionary."""
        amenity_instance = cls(**obj_dict)
        return amenity_instance
