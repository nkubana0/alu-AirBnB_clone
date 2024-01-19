#!/usr/bin/python3

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def test_create_instance(self):
        """Test creating an instance of Place."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        """Test attributes of the Place class."""
        place = Place(name='Cozy Cabin', price=100, city_id='123', user_id='456')
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'price'))
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))

    def test_to_dict(self):
        """Test converting Place instance to dictionary."""
        place = Place(name='Cozy Cabin', price=100, city_id='123', user_id='456')
        place_dict = place.to_dict()
        self.assertEqual(place_dict['name'], 'Cozy Cabin')
        self.assertEqual(place_dict['price'], 100)
        self.assertEqual(place_dict['city_id'], '123')
        self.assertEqual(place_dict['user_id'], '456')

    def test_from_dict(self):
        """Test creating a Place instance from dictionary."""
        place_dict = {'name': 'Cozy Cabin', 'price': 100, 'city_id': '123', 'user_id': '456'}
        place = Place.from_dict(place_dict)
        self.assertIsInstance(place, Place)
        self.assertEqual(place.name, 'Cozy Cabin')
        self.assertEqual(place.price, 100)
        self.assertEqual(place.city_id, '123')
        self.assertEqual(place.user_id, '456')

if __name__ == '__main__':
    unittest.main()
