#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """

    def test_save_and_reload(self):
        """Test saving and reloading objects."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        storage.reload()

        all_objects = storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), all_objects)

if __name__ == '__main__':
    unittest.main()
