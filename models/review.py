#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """Review class."""
    def __init__(self, text="", user_id="", place_id="", **kwargs):
        super().__init__(**kwargs)
        self.text = text
        self.user_id = user_id
        self.place_id = place_id

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a Review instance from a dictionary."""
        review_instance = cls(**obj_dict)
        return review_instance
