#!/usr/bin/python3

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
