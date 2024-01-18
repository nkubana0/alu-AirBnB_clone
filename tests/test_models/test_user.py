#!/usr/bin/python3
"""Unit tests for User class"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_init(self):
        """Test initialization of User"""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))
