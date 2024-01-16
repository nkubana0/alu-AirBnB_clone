#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_create_instance(self):
        """Test creating an instance of BaseModel."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_to_dict(self):
        """Test converting BaseModel instance to dictionary."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

    def test_from_dict(self):
        """Test creating a BaseModel instance from dictionary."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel.from_dict(obj_dict)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertEqual(new_obj.id, obj.id)

    def test_to_json_string(self):
        """Test converting BaseModel instance to JSON string."""
        obj = BaseModel()
        json_str = obj.to_json_string()
        self.assertIsInstance(json_str, str)
        self.assertIn("BaseModel", json_str)

    def test_from_json_string(self):
        """Test creating a BaseModel instance from JSON string."""
        obj = BaseModel()
        json_str = obj.to_json_string()
        new_obj = BaseModel.from_json_string(json_str)
        self.assertIsInstance(new_obj, BaseModel)
        self.assertEqual(new_obj.id, obj.id)

if __name__ == '__main__':
    unittest.main()
