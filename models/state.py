#!/usr/bin/python3

# models/state.py

from models.base_model import BaseModel

class State(BaseModel):
    """State class that inherits from BaseModel."""
    
    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        super().__init__(*args, **kwargs)
        # Add any additional attributes specific to the State class here

    def to_dict(self):
        """Return a dictionary representation of the State object."""
        obj_dict = super().to_dict()
        # Add any specific attributes from State class to the dictionary here
        return obj_dict

    # Add any specific methods for the State class here

    @property
    def id(self):
        """Getter method for the 'id' attribute."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter method for the 'id' attribute."""
        self._id = value
