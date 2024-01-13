#!/usr/bin/python3
"""Unittest for FileStorage class"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""
    def setUp(self):
        """Set up for test"""
        self.file_storage = FileStorage()

    def test_all(self):
        """Test all() method"""
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertIs(objects, self.file_storage._FileStorage__objects)

    def test_new(self):
        """Test new() method"""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.file_storage.new(obj)
        self.assertIn(key, self.file_storage.all())

    def test_save_reload(self):
        """Test save() and reload() methods"""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.file_storage.new(obj)
        self.file_storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(key, new_storage.all())

if __name__ == '__main__':
    unittest.main()
