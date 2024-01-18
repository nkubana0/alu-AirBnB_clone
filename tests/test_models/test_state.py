#!/usr/bin/python3
"""Unit tests for State class"""
import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Test cases for State class"""

    def test_init(self):
        """Test initialization of State"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))
