#!/usr/bin/python3
"""
This module contains the User class (Blueprint for creating user objects).
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    This is the user class.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialize public instance attributes.
        """
        super().__init__(*args, **kwargs)

        # self.email = User.email
        # self.password = User.password
        # self.first_name = User.first_name
        # self.last_name = User.last_name
