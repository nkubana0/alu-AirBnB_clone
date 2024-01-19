#!/usr/bin/python3

from models.user import User
import unittest

class TestUser(unittest.TestCase):
    def test_create_instance(self):
        user = User(email='test@example.com', password='password')
        self.assertIsInstance(user, User)
