#!/usr/bin/python3
'''Test class for the `Amenity` class
'''
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenityClass(unittest.TestCase):
    '''TestAmenityClass: defines tests for `Amenity` objects
    '''

    def test_inherits_from_BaseModel(self):
        '''Ensures that `Amenity` objects inherit from BaseModel
        '''
        amenity_instance = Amenity()
        self.assertIsInstance(amenity_instance, BaseModel)

    def test_has_name_attribute(self):
        '''Ensures `Amenity` object has the attribute `name`
        '''
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_name_attribute_type_str(self):
        '''Ensures the `name` attribute is of type str
        '''
        self.assertIsInstance(Amenity.name, str)


if __name__ == "__main__":
    unittest.main()
