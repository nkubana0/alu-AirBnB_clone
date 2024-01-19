#!/usr/bin/python3

from models.base_model import BaseModel
from datetime import datetime

class State(BaseModel):
    """State class that inherits from BaseModel."""
    
    def __init__(self, *args, **kwargs):
        """Initialize State instance."""
        super().__init__(*args, **kwargs)
        # Add any additional attributes specific to the State class here
        self.name = kwargs.get('name', '')  # Add any default value for the name attribute

    def to_dict(self):
        """Return a dictionary representation of the State object."""
        obj_dict = super().to_dict()
        # Add any specific attributes from State class to the dictionary here
        obj_dict['name'] = self.name
        return obj_dict

    # Add any specific methods for the State class here

    @property
    def id(self):
        """Getter method for the 'id' attribute."""
        return self.__dict__.get('id')

    @id.setter
    def id(self, value):
        """Setter method for the 'id' attribute."""
        self.__dict__['id'] = value

    @property
    def created_at(self):
        """Getter method for the 'created_at' attribute."""
        return self.__dict__.get('created_at')

    @created_at.setter
    def created_at(self, value):
        """Setter method for the 'created_at' attribute."""
        self.__dict__['created_at'] = value

    @property
    def updated_at(self):
        """Getter method for the 'updated_at' attribute."""
        return self.__dict__.get('up
