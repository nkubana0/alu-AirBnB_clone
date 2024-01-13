#!/usr/bin/python3
"""Unittest for Review class"""
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Test cases for Review class"""
    def test_instance(self):
        """Test instance creation"""
        review = Review()
        self.assertIsInstance(review, Review)

if __name__ == '__main__':
    unittest.main()
