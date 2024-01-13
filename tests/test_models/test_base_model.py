#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""
    def test_instance(self):
        """Test instance creation"""
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)

    def test_id_generation(self):
        """Test id generation"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_to_dict(self):
        """Test to_dict method"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(type(base_model_dict), dict)
        self.assertIn('__class__', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

    def test_str_representation(self):
        """Test __str__ method"""
        base_model = BaseModel()
        str_representation = str(base_model)
        self.assertTrue('[BaseModel]' in str_representation)
        self.assertTrue('id' in str_representation)
        self.assertTrue('created_at' in str_representation)
        self.assertTrue('updated_at' in str_representation)

if __name__ == '__main__':
    unittest.main()
