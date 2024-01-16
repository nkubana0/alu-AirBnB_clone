#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    """Place class."""
    def __init__(self, name="", price=0, city_id="", user_id="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.price = price
        self.city_id = city_id
        self.user_id = user_id

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a Place instance from a dictionary."""
        place_instance = cls(**obj_dict)
        return place_instance
