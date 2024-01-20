#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage

class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def test_save_and_reload(self):
        """Test saving and reloading objects."""
        storage = FileStorage()
        obj = Place()
        storage.new(obj)
        storage.save()
        storage.reload()

        all_objects = storage.all()
        self.assertIn("Place.{}".format(obj.id), all_objects)

if __name__ == '__main__':
    unittest.main()
