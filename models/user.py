#!/usr/bin/python3

import uuid
from datetime import datetime

class User:
    def __init__(self, email, password, first_name=None, last_name=None, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        user_dict = {
            '__class__': self.__class__.__name__,
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
        return user_dict

    @classmethod
    def from_dict(cls, user_dict):
        # Assuming the structure of the dictionary is compatible with the __init__ method
        return cls(**user_dict)
