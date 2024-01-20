#!/usr/bin/python3

from models.base_model import BaseModel

class State(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get('name', '')
