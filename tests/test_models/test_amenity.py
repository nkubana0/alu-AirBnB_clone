#!/usr/bin/python3

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def test_create_instance(self):
        """Test creating an instance of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        """Test attributes of the Amenity class."""
        amenity = Amenity(name='WiFi')
        self.assertTrue(hasattr(amenity, 'name'))

    def test_to_dict(self):
        """Test converting Amenity instance to dictionary."""
        amenity = Amenity(name='WiFi')
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['name'], 'WiFi')

    def test_from_dict(self):
        """Test creating an Amenity instance from dictionary."""
        amenity_dict = {'name': 'WiFi'}
        amenity = Amenity.from_dict(amenity_dict)
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, 'WiFi')

if __name__ == '__main__':
    unittest.main()
