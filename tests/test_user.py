#!/usr/bin/python3
"""Unittest for User class"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Test cases for User class"""
    def test_instance(self):
        """Test instance creation"""
        user = User()
        self.assertIsInstance(user, User)

if __name__ == '__main__':
    unittest.main()
