#!/usr/bin/python3

import uuid
from datetime import datetime
import json
from models.engine.file_storage import FileStorage

class BaseModel:
    __file_path = "file.json"
    __objects = FileStorage()

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        self.__class__.__objects.new(self)
        self.__class__.__objects.save()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def to_json_string(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_dict(cls, obj_dict):
        if "__class__" in obj_dict:
            cls_name = obj_dict.pop("__class__")
            if cls_name == cls.__name__:
                return cls(**obj_dict)
        return None

    @classmethod
    def from_json_string(cls, json_str):
        obj_dict = json.loads(json_str)
        return cls.from_dict(obj_dict)

    @classmethod
    def save(cls):
        cls.__objects.save()

    @classmethod
    def reload(cls):
        cls.__objects.reload()
