#!/usr/bin/python3
"""Unit tests for BaseModel class"""
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_init(self):
        """Test initialization of BaseModel"""
        base = BaseModel()
        self.assertTrue(hasattr(base, 'id'))
        self.assertTrue(hasattr(base, 'created_at'))
        self.assertTrue(hasattr(base, 'updated_at'))
