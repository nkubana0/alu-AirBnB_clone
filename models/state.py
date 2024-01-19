#!/usr/bin/python3

from models.base_model import BaseModel

class State(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')  # Add other State-specific attributes here if needed

    def to_dict(self):
        """Return a dictionary representation of the object."""
        obj_dict = super().to_dict()
        obj_dict['name'] = self.name
        return obj_dict
