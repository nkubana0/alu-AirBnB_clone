#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
}

storage = FileStorage()
storage.reload()

