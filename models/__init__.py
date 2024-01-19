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
