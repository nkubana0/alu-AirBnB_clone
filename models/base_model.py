#!/usr/bin/python3

from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key in ["created_at", "updated_at"]:
                if isinstance(value, str):
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
            else:
                setattr(self, key, value)

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, str(self.to_dict())
        )
