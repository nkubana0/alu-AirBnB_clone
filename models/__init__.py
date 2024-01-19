#!/usr/bin/python3

from models.engine.file_storage import FileStorage

classes = {
    'BaseModel': BaseModel,  # Add other classes as needed
    'User': User,
    'State': State,
    # Add more classes as needed
}

storage = FileStorage()
storage.reload()

