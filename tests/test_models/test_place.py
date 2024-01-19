#!/usr/bin/python3

from models.place import Place
import unittest
from datetime import datetime
import uuid

class TestPlace(unittest.TestCase):
    """Test cases for Place class."""

    def test_to_dict(self):
        """Test converting Place instance to dictionary."""
        place = Place(
            id=str(uuid.uuid4()),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            name='Cozy Cabin',
            # Include other required attributes for Place here
        )

        place_dict = place.to_dict()

        # Ensure that 'name' is in the dictionary
        self.assertIn('name', place_dict)
        self.assertEqual(place_dict['name'], 'Cozy Cabin')
