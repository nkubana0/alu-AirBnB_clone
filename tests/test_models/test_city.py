#!/usr/bin/python3
"""Unit tests for City class"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_init(self):
        """Test initialization of City"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
