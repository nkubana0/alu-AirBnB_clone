#!/usr/bin/python3

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """
    Test cases for the User class.
    """

    def test_create_instance(self):
        """Test creating an instance of User."""
        user = User()
        self.assertIsInstance(user, User)

    def test_attributes(self):
        """Test attributes of the User class."""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_to_dict(self):
        """Test converting User instance to dictionary."""
        user = User(email='test@example.com', password='password', first_name='John', last_name='Doe')
        user_dict = user.to_dict()
        self.assertEqual(user_dict['email'], 'test@example.com')
        self.assertEqual(user_dict['password'], 'password')
        self.assertEqual(user_dict['first_name'], 'John')
        self.assertEqual(user_dict['last_name'], 'Doe')

    def test_from_dict(self):
        """Test creating a User instance from dictionary."""
        user_dict = {'email': 'test@example.com', 'password': 'password', 'first_name': 'John', 'last_name': 'Doe'}
        user = User.from_dict(user_dict)
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'password')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')

if __name__ == '__main__':
    unittest.main()
