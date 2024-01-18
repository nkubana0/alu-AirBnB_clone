#!/usr/bin/python3
"""Unit tests for Review class"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_init(self):
        """Test initialization of Review"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))
