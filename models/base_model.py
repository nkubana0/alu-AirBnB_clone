#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def to_dict(self):
        """Return a dictionary representation of the object."""
        obj_dict = {
            '__class__': self.__class__.__name__,
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
        return obj_dict

    def save(self):
        """Save the object and call save(self) method of storage."""
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """Return the string representation of the object."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.to_dict()
        )

from models import storage
