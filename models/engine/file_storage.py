#!/usr/bin/python3

import json
from os import path

class FileStorage:
    """
    This class handles serialization and deserialization of objects to and from a JSON file.
    """

    def __init__(self):
        """
        Initialize the FileStorage instance.
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        Retrieve all stored objects.

        Returns:
            dict: A dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to storage.

        Args:
            obj: The object to be added to storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Save serialized objects to a JSON file.
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Reload objects from a JSON file.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, obj_data in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    module_name = f"models.{class_name.lower()}"
                    class_obj = getattr(__import__(module_name, fromlist=[class_name]), class_name)
                    obj_instance = class_obj(**obj_data)
                    self.__objects[key] = obj_instance

