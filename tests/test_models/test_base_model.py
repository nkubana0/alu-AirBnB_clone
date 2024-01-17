import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
        def test_create_instance(self):
            obj = BaseModel()
            self.assertIsInstance(obj, BaseModel)

        def test_id_generation(self):
            obj1 = BaseModel()
            obj2 = BaseModel()
            self.assertNotEqual(obj1.id, obj2.id)

        def test_timestamps(self):
            obj = BaseModel()
            self.assertIsInstance(obj.created_at, datetime)
            self.assertIsInstance(obj.updated_at, datetime)
            self.assertEqual(obj.created_at, obj.updated_at)

        def test_to_dict_method(self):
            obj = BaseModel()
            dict_copy = obj.__dict__.copy()
            dict_copy['_class_'] = obj.__class__.__name__
            dict_copy['created_at'] = dict_copy['created_at'].isoformat()
            dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
                    
            self.assertEqual(obj.to_dict(), dict_copy)

        def test_from_dict_method(self):
            obj = BaseModel()
            obj_dict = obj.to_dict()
            new_obj = BaseModel(**obj_dict)
            self.assertEqual(obj.id, new_obj.id)
            self.assertEqual(obj.created_at, new_obj.created_at)
            self.assertEqual(obj.updated_at, new_obj.updated_at)

if __name__ == '__main__':
        unittest.main()
