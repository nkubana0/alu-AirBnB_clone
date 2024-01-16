#!/usr/bin/python

from models.base_model import BaseModel

class User(BaseModel):
    """User class."""
    def __init__(self, email="", password="", first_name="", last_name="", **kwargs):
        super().__init__(**kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a User instance from a dictionary."""
        user_instance = cls(**obj_dict)
        return user_instance
