#!/usr/bin/python3
"""FileStorage module"""
import json
import os
from models.base_model import BaseModel

class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON and save to file"""
        json_dict = {}
        for key, value in self.__objects.items():
            json_dict[key] = value.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(json_dict, file)

    def reload(self):
        """Deserialize JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_dict = json.load(file)
                for key, value in json_dict.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
