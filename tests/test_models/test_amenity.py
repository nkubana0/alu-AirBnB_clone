#!/usr/bin/python3
"""Unit tests for Amenity class"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class"""

    def test_init(self):
        """Test initialization of Amenity"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
