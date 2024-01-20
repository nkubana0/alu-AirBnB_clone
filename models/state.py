#!/usr/bin/python3

from models.base_model import BaseModel

class State(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get('name', '')

    def to_dict(self):
        """Return a dictionary representation of the object."""
        obj_dict = super().to_dict()
        obj_dict['name'] = self.name
        return obj_dict

    @classmethod
    def from_dict(cls, obj_dict):
        """Create a new instance from a dictionary."""
        if obj_dict is None or not isinstance(obj_dict, dict):
            return None

        state = cls()
        state.name = obj_dict.get('name', '')
        return state
