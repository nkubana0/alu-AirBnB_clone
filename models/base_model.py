#!/usr/bin/python3
"""
This module defines a BaseModel class that
defines all common attributes/methods for model classes
"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """
    This is the base model class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize public instance attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Updates the file storage with the new/updated information.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the object to a dictionary representation.

        Returns:
            dict: A dictionary representation of the object.
        """

        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                value = value.isoformat()
            obj_dict[key] = value

        return obj_dict

    def __str__(self):
        """
        Returns a string representation of the BaseModel class.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
