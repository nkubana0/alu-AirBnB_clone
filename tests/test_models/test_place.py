#!/usr/bin/python3
"""Unit tests for Place class"""
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def test_init(self):
        """Test initialization of Place"""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
