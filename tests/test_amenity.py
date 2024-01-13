#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""
    def test_instance(self):
        """Test instance creation"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

if __name__ == '__main__':
    unittest.main()
