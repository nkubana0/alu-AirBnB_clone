#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_str_returns_correct_format(self):
        base_model = BaseModel(id='4629852b-8345-473d-a679-a894f897c56e',
                               created_at=datetime(2024, 1, 19, 11, 28, 14, 65377),
                               updated_at=datetime(2024, 1, 19, 11, 28, 14, 65377))
        str_representation = str(base_model)

        # Check if the relevant information is present in the string representation
        self.assertIn(base_model.id, str_representation)
        self.assertIn(str(base_model.created_at), str_representation)
        self.assertIn(str(base_model.updated_at), str_representation)
        self.assertIn(base_model.__class__.__name__, str_representation)

if __name__ == '__main__':
    unittest.main()

