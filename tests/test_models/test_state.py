#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def test_create_instance(self):
        """Test creating an instance of State."""
        state = State()
        self.assertIsInstance(state, State)

    def test_attributes(self):
        """Test attributes of the State class."""
        state = State(name='California')
        self.assertTrue(hasattr(state, 'name'))

    def test_to_dict(self):
        """Test converting State instance to dictionary."""
        state = State(name='California')
        state_dict = state.to_dict()
        self.assertEqual(state_dict['name'], 'California')

    def test_from_dict(self):
        """Test creating a State instance from dictionary."""
        state_dict = {'name': 'California'}
        state = State.from_dict(state_dict)
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, 'California')

if __name__ == '__main__':
    unittest.main()
