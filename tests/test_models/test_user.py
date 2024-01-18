#!/user/bin/python3
'''Defines tests for the User class.
'''
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUserClass(unittest.TestCase):
    '''TestUserClass: Tests class for the User class.
    '''

    def setUp(self):
        '''Sets up variables for subsequent tests.
        '''
        self.test_user_instance = User()
        self.test_user_instance.save()

    def test_inherits_from_BaseModel(self):
        '''Tests that `User` class inherits from BaseModel.
        '''
        self.assertIsInstance(self.test_user_instance, BaseModel)

    def test_has_email_attribute(self):
        '''Tests if `User` object has the email attribute.
        '''
        self.assertTrue(hasattr(User, 'email'))

    def test_email_attribute_type_str(self):
        '''Tests if the `email` attribute is of type str.
        '''
        self.assertIsInstance(User.email, str)

    def test_has_password_attribute(self):
        '''Tests if `User` object has the password attribute.
        '''
        self.assertTrue(hasattr(User, 'password'))

    def test_password_attribute_type_str(self):
        '''Tests if the `password` attribute is of type str.
        '''
        self.assertIsInstance(User.password, str)

    def test_has_first_name_attribute(self):
        '''Tests if `User` object has the first_name attribute.
        '''
        self.assertTrue(hasattr(User, 'first_name'))

    def test_first_name_attribute_type_str(self):
        '''Tests if the `first_name` attribute is of type str.
        '''
        self.assertIsInstance(User.first_name, str)

    def test_has_last_name_attribute(self):
        '''Tests if `User` object has the last_name attribute.
        '''
        self.assertTrue(hasattr(User, 'last_name'))

    def test_last_name_attribute_type_str(self):
        '''Tests if the `last_name` attribute is of type str.
        '''
        self.assertIsInstance(User.last_name, str)


if __name__ == "__main__":
    unittest.main()
