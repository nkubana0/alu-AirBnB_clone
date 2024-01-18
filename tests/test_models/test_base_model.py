'''Test file for the 'BaseModel' class
'''

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    '''TestBaseModelClass for testing the 'BaseModel' class.
    '''

    def test_id_created_updated_attributes_privacy(self):
        '''Tests privacy of 'id', 'created_at', and 'updated_at' attributes.
        '''
        base_instance = BaseModel()
        with self.assertRaises(AttributeError):
            try:
                _ = base_instance.id
                _ = base_instance.created_at
                _ = base_instance.updated_at
            except AttributeError:
                pass
            else:
                raise AttributeError

    def test_string_representation_format(self):
        '''Tests the format of the string
        representation of a 'BaseModel' object.
        '''
        base_instance = BaseModel()
        expected_string = "[{}] ({}) {}".format(
            base_instance.__class__.__name__,
            base_instance.id,
            base_instance.__dict__
        )
        self.assertEqual(str(base_instance), expected_string)

    def test_id_type_is_string(self):
        '''Tests if the 'id' attribute has a type of string.
        '''
        base_instance = BaseModel()
        self.assertIs(type(base_instance.id), str)

    def test_current_datetime_setting(self):
        '''Tests if 'created_at' and 'updated_at'
        attributes are set to the current time.
        '''
        base_instance = BaseModel()
        current_datetime = datetime.now()\
            .strftime("%Y-%m-%d %H:%M:%S")
        self.assertEqual(base_instance.created_at.strftime(
            "%Y-%m-%d %H:%M:%S"
            ),
              current_datetime
              )
        self.assertEqual(base_instance.updated_at.strftime(
            "%Y-%m-%d %H:%M:%S"
            ),
              current_datetime
              )

    def test_id_exists_in_dict_representation(self):
        '''Tests if 'id' exists in the dictionary
        representation and has a unique ID value.
        '''
        base_instance = BaseModel()
        obj_dict = base_instance.to_dict()
        self.assertIn('id', obj_dict.keys())
        self.assertIsNotNone(obj_dict['id'])

    def test_class_key_in_dict_representation(self):
        '''Tests if the '__class__' key is added
        to the dictionary representation.
        '''
        base_instance = BaseModel()
        obj_dict = base_instance.to_dict()
        self.assertIn('__class__', obj_dict.keys())

    def test_created_and_updated_time_format_in_dict_representation(self):
        '''Tests the string format of 'created_at' and
        'updated_at' keys in the dictionary representation.
        '''
        base_instance = BaseModel()
        format_created = base_instance.created_at\
            .strftime("%Y-%m-%dT%H:%M:%S.%f")
        format_updated = base_instance.updated_at\
            .strftime("%Y-%m-%dT%H:%M:%S.%f")
        obj_dict = base_instance.to_dict()
        self.assertEqual(obj_dict['created_at'], format_created)
        self.assertEqual(obj_dict['updated_at'], format_updated)

    def test_updated_time_after_save(self):
        '''Tests if 'updated_at' attribute is
        updated after calling save().
        '''
        base_instance = BaseModel()
        prev_time = base_instance.updated_at\
            .strftime("%Y-%m-%dT%H:%M:%S.%f")
        base_instance.save()
        curr_time = base_instance.updated_at.\
            strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.assertNotEqual(prev_time, curr_time)

    def test_initialization_using_kwargs(self):
        '''Tests if 'BaseModel' object can be
        initialized using a dictionary.
        '''
        init_dict = {
            'id': '123456789',
            'created_at': '2022-08-29T11:23:12.283000',
            'updated_at': '2022-08-29T11:23:12.283000'
        }
        base_instance = BaseModel(**init_dict)
        base_dict = base_instance.__dict__
        self.assertIs(type(base_instance.id), str)
        self.assertIs(type(base_instance.created_at), datetime)
        self.assertIs(type(base_instance.created_at), datetime)
        self.assertIsNotNone(base_instance.id)
        self.assertIsNotNone(base_instance.created_at)
        self.assertIsNotNone(base_instance.updated_at)
        self.assertNotIn('__class__', base_dict.keys())


if __name__ == '__main__':
    unittest.main()
