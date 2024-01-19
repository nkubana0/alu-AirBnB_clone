#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    cls = globals()[class_name]
                    obj = cls(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
