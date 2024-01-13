#!/usr/bin/python3
"""Unittest for Place class"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for Place class"""
    def test_instance(self):
        """Test instance creation"""
        place = Place()
        self.assertIsInstance(place, Place)

if __name__ == '__main__':
    unittest.main()
