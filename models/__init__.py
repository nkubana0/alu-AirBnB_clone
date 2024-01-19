#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

classes = {
    'BaseModel': BaseModel,  # Add other classes as needed
    'User': User,
    'State': State,
    # Add more classes as needed
}

storage = FileStorage()
storage.reload()

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


