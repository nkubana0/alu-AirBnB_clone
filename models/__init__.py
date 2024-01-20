#!/usr/bin/python3

from models.engine.file_storage import FileStorage

storage = FileStorage()

# Import the classes after initializing storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
# Add other imports as needed

storage.reload()
