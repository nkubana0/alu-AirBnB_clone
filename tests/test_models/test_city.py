#!/usr/bin/python3

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def test_create_instance(self):
        """Test creating an instance of City."""
        city = City()
        self.assertIsInstance(city, City)

    def test_attributes(self):
        """Test attributes of the City class."""
        city = City(name='San Francisco')
        self.assertTrue(hasattr(city, 'name'))

    def test_to_dict(self):
        """Test converting City instance to dictionary."""
        city = City(name='San Francisco')
        city_dict = city.to_dict()
        self.assertEqual(city_dict['name'], 'San Francisco')

    def test_from_dict(self):
        """Test creating a City instance from dictionary."""
        city_dict = {'name': 'San Francisco'}
        city = City.from_dict(city_dict)
        self.assertIsInstance(city, City)
        self.assertEqual(city.name, 'San Francisco')

if __name__ == '__main__':
    unittest.main()
