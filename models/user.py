#!/usr/bin/python

import uuid
from datetime import datetime

class User:
    def __init__(self, email, password, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.email = email
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        user_dict = {
            '__class__': self.__class__.__name__,
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
        return user_dict

