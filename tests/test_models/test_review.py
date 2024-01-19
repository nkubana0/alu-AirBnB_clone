#!/usr/bin/python3

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def test_create_instance(self):
        """Test creating an instance of Review."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        """Test attributes of the Review class."""
        review = Review(text='Great place!', user_id='123', place_id='456')
        self.assertTrue(hasattr(review, 'text'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'place_id'))

    def test_to_dict(self):
        """Test converting Review instance to dictionary."""
        review = Review(text='Great place!', user_id='123', place_id='456')
        review_dict = review.to_dict()
        self.assertEqual(review_dict['text'], 'Great place!')
        self.assertEqual(review_dict['user_id'], '123')
        self.assertEqual(review_dict['place_id'], '456')

    def test_from_dict(self):
        """Test creating a Review instance from dictionary."""
        review_dict = {'text': 'Great place!', 'user_id': '123', 'place_id': '456'}
        review = Review.from_dict(review_dict)
        self.assertIsInstance(review, Review)
        self.assertEqual(review.text, 'Great place!')
        self.assertEqual(review.user_id, '123')
        self.assertEqual(review.place_id, '456')

if __name__ == '__main__':
    unittest.main()
