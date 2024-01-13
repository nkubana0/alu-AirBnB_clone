#!/usr/bin/python3
"""Unittest for City class"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for City class"""
    def test_instance(self):
        """Test instance creation"""
        city = City()
        self.assertIsInstance(city, City)

if __name__ == '__main__':
    unittest.main()
