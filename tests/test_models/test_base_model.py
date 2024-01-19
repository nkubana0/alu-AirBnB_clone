#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

def main_execution_logic():
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)

    my_model.save()
    print(my_model)

    my_model_json = my_model.to_dict()
    print(my_model_json)

    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

class TestBaseModel(unittest.TestCase):

    def test_save_updates_updated_at(self):
        base_model = BaseModel()
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(initial_updated_at, base_model.updated_at)

    def test_to_dict_returns_correct_dictionary(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertIsInstance(base_model_dict, dict)
        self.assertIn('__class__', base_model_dict)
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)

    def test_str_returns_correct_format(self):
        base_model = BaseModel()
        str_representation = str(base_model)
        self.assertIn(base_model.__class__.__name__, str_representation)
        self.assertIn(base_model.id, str_representation)
        self.assertIn(str(base_model.__dict__), str_representation)

if __name__ == '__main__':
    main_execution_logic()
    unittest.main()
