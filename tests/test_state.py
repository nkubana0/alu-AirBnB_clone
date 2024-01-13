#!/usr/bin/python3
"""Unittest for State class"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for State class"""
    def test_instance(self):
        """Test instance creation"""
        state = State()
        self.assertIsInstance(state, State)

if __name__ == '__main__':
    unittest.main()
