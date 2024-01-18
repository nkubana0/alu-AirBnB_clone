'''Test file for the 'State' class definition.
'''
import unittest
from models.base_model import BaseModel
from models.state import State


class TestStateClass(unittest.TestCase):
    ''''TestStateClass' class. Used to test
    the definition of the 'State' class.
    '''
    def setUp(self):
        '''Sets up variables for use in later parts of the test.
        '''
        self.test_state_instance = State()
        self.test_state_instance.save()

    def test_inherits_from_BaseModel(self):
        '''Test if the instance of class 'State' inherits from 'BaseModel'.
        '''
        self.assertIsInstance(self.test_state_instance, BaseModel)

    def test_has_name_attribute(self):
        '''Test if the 'State' class has the 'name' attribute.
        '''
        self.assertTrue(hasattr(State, "name"))

    def test_name_attribute_type_str(self):
        '''Tests the type of the 'name' attribute in the 'State' class.
        '''
        self.assertIsInstance(State.name, str)


if __name__ == '__main__':
    unittest.main()
