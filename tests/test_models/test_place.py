#!/usr/bin/python3
'''Defines tests for the `Place` class.
'''
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    '''TestPlaceClass: Inherits from unittest and tests the `Place` class.
    '''

    def setUp(self):
        '''Set up initializations before running tests.
        '''
        self.test_place_instance = Place()

    def test_inherits_from_BaseModel(self):
        '''Test if `Place` inherits from BaseModel.
        '''
        self.assertIsInstance(self.test_place_instance, BaseModel)

    def test_has_city_id_attribute(self):
        '''Test if `Place` class has the `city_id` attribute.
        '''
        self.assertTrue(hasattr(Place, 'city_id'))

    def test_city_id_attribute_type_str(self):
        '''Test if `city_id` attribute in `Place` class is of type str.
        '''
        self.assertIsInstance(Place.city_id, str)

    def test_has_user_id_attribute(self):
        '''Test if `Place` class has the `user_id` attribute.
        '''
        self.assertTrue(hasattr(Place, 'user_id'))

    def test_user_id_attribute_type_str(self):
        '''Test if `user_id` attribute in `Place` class is of type str.
        '''
        self.assertIsInstance(Place.user_id, str)

    def test_has_name_attribute(self):
        '''Test if `Place` class has the `name` attribute.
        '''
        self.assertTrue(hasattr(Place, 'name'))

    def test_name_attribute_type_str(self):
        '''Test if `name` attribute in `Place` class is of type str.
        '''
        self.assertIsInstance(Place.name, str)

    def test_has_description_attribute(self):
        '''Test if `Place` class has the `description` attribute.
        '''
        self.assertTrue(hasattr(Place, 'description'))

    def test_description_attribute_type_str(self):
        '''Test if `description` attribute in `Place` class is of type str.
        '''
        self.assertIsInstance(Place.description, str)

    def test_has_number_rooms_attribute(self):
        '''Test if `Place` class has the `number_rooms` attribute.
        '''
        self.assertTrue(hasattr(Place, 'number_rooms'))

    def test_number_rooms_attribute_type_int(self):
        '''Test if `number_rooms` attribute in `Place` class is of type int.
        '''
        self.assertIsInstance(Place.number_rooms, int)

    def test_has_number_bathrooms_attribute(self):
        '''Test if `Place` class has the `number_bathrooms` attribute.
        '''
        self.assertTrue(hasattr(Place, 'number_bathrooms'))

    def test_number_bathrooms_attribute_type_int(self):
        '''Test if `number_bathrooms`
        attribute in `Place` class is of type int.
        '''
        self.assertIsInstance(Place.number_bathrooms, int)

    def test_has_max_guest_attribute(self):
        '''Test if `Place` class has the `max_guest` attribute.
        '''
        self.assertTrue(hasattr(Place, 'max_guest'))

    def test_max_guest_attribute_type_int(self):
        '''Test if `max_guest` attribute in `Place` class is of type int.
        '''
        self.assertIsInstance(Place.max_guest, int)

    def test_has_price_by_night_attribute(self):
        '''Test if `Place` class has the `price_by_night` attribute.
        '''
        self.assertTrue(hasattr(Place, 'price_by_night'))

    def test_price_by_night_attribute_type_int(self):
        '''Test if `price_by_night` attribute in `Place` class is of type int.
        '''
        self.assertIsInstance(Place.price_by_night, int)

    def test_has_latitude_attribute(self):
        '''Test if `Place` class has the `latitude` attribute.
        '''
        self.assertTrue(hasattr(Place, 'latitude'))

    def test_latitude_attribute_type_float(self):
        '''Test if `latitude` attribute in `Place` class is of type float.
        '''
        self.assertIsInstance(Place.latitude, float)

    def test_has_longitude_attribute(self):
        '''Test if `Place` class has the `longitude` attribute.
        '''
        self.assertTrue(hasattr(Place, 'longitude'))

    def test_longitude_attribute_type_float(self):
        '''Test if `longitude` attribute in `Place` class is of type float.
        '''
        self.assertIsInstance(Place.longitude, float)

    def test_has_amenity_ids_attribute(self):
        '''Test if `Place` class has the `amenity_ids` attribute.
        '''
        self.assertTrue(hasattr(Place, 'amenity_ids'))

    def test_amenity_ids_attribute_type_list(self):
        '''Test if `amenity_ids` attribute in `Place` class is of type list.
        '''
        self.assertIsInstance(Place.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
