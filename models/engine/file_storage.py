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
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = key.split('.')[0]
                    if class_name in globals():
                        cls = globals()[class_name]
                        instance = cls(**value)
                        self.__objects[key] = instance
        except FileNotFoundError:
            pass
