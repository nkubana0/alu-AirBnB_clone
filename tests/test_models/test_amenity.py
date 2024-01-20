#!/usr/bin/python3

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_to_dict(self):
        amenity = Amenity(name='WiFi')
        amenity_dict = amenity.to_dict()

        self.assertIn('name', amenity_dict)
        self.assertIn('__class__', amenity_dict)

if __name__ == '__main__':
    unittest.main()
