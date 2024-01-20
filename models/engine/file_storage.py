#!/usr/bin/python3

import json
from models.base_model import BaseModel

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
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)

            for key, value in obj_dict.items():
                cls_name = value['__class__']
                cls = getattr(__import__('models'), cls_name)

                if cls:
                    instance = cls(**value)
                    storage.new(instance)

        except FileNotFoundError:
            pass
