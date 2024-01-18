#!/usr/bin/python3
"""
defines all common attributes for other classes
"""

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, id, created_at, updated_at):
        """
        initialising
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        updates updated_at to ccurrent time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all key values
        """
        __class__ :self.__class__.__name__
        dict_representation : self.__dict__.copy()
        dict_representation['__clas__'] : class_name
        dict_representation['created_at'] : self.created.isoformat()
        dict_representation['updated_at'] : self.updated_at.isoformat()
        return dict_represenation

    def __str__(self):
        """
        returns a string representation of the instance
        """
        class_name= self.__class__.__name__
        return "[{}] ({}) {}".format(class_name,self.id, self.__dict__
