#!/usr/bin/python3

from models.base_model import BaseModel

class State(BaseModel):
    """State class that inherits from BaseModel."""
    
    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Return a dictionary representation of the State object."""
        obj_dict = super().to_dict()
        return obj_dict

    @property
    def id(self):
        """Getter method for the 'id' attribute."""
        return super().id

    @id.setter
    def id(self, value):
        """Setter method for the 'id' attribute."""
        super(State, type(self)).id.fset(self, value)
