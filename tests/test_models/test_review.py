#!/usr/bin/python3
'''Defines tests for the `Review` class.
'''
from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReviewClass(unittest.TestCase):
    '''TestReviewClass: Defines tests for the `Review` class.
    '''

    def test_inherits_from_BaseModel(self):
        '''Test ensures `Review` inherits from BaseModel.
        '''
        test_review_instance = Review()
        self.assertIsInstance(test_review_instance, BaseModel)

    def test_has_place_id_attribute(self):
        '''Test ensures `place_id` attribute exists in `Review` class.
        '''
        self.assertTrue(hasattr(Review, 'place_id'))

    def test_place_id_attribute_type_str(self):
        '''Test ensures `place_id` attribute in `Review` class is of type str.
        '''
        self.assertIsInstance(Review.place_id, str)

    def test_has_user_id_attribute(self):
        '''Test ensures `user_id` attribute exists in `Review` class.
        '''
        self.assertTrue(hasattr(Review, 'user_id'))

    def test_user_id_attribute_type_str(self):
        '''Test ensures `user_id` attribute in `Review` class is of type str.
        '''
        self.assertIsInstance(Review.user_id, str)

    def test_has_text_attribute(self):
        '''Test ensures `text` attribute exists in `Review` class.
        '''
        self.assertTrue(hasattr(Review, 'text'))

    def test_text_attribute_type_str(self):
        '''Test ensures `text` attribute in `Review` class is of type str.
        '''
        self.assertIsInstance(Review.text, str)


if __name__ == "__main__":
    unittest.main()
