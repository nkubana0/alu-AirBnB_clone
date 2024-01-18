'''Tests for the 'City' class definition.
'''
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCityClass(unittest.TestCase):
    '''TestCityClass: Tests the definition of the 'City' class.
    '''

    def setUp(self):
        '''Sets up variables for use in later tests.
        '''
        self.city_instance = City()
        self.city_instance.save()

    def test_inherits_from_BaseModel(self):
        '''Tests if an instance of the 'City' class inherits from 'BaseModel'
        '''
        self.assertIsInstance(self.city_instance, BaseModel)

    def test_has_name_attribute(self):
        '''Tests that the 'City' class has a 'name' attribute
        '''
        self.assertTrue(hasattr(City, "name"))

    def test_name_attribute_type_str(self):
        '''Tests the type of the 'name' attribute in the 'City' class.
        '''
        self.assertIsInstance(City.name, str)

    def test_has_state_id_attribute(self):
        '''Tests that the 'City' class has a 'state_id' attribute
        '''
        self.assertTrue(hasattr(City, "state_id"))

    def test_state_id_attribute_type_str(self):
        '''Tests the type of the 'state_id' attribute in the 'City' class.
        '''
        self.assertIsInstance(City.state_id, str)


if __name__ == '__main__':
    unittest.main()
