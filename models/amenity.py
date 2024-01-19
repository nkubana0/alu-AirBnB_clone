#!/usr/bin/python3

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_to_dict(self):
        amenity = Amenity(name='WiFi')  # Replace with your Amenity instance creation
        amenity_dict = amenity.to_dict()

        # Check if the expected keys are present in the dictionary
        self.assertIn('name', amenity_dict)
        self.assertIn('__class__', amenity_dict)

        # Additional assertions based on your Amenity class attributes

if __name__ == '__main__':
    unittest.main()
