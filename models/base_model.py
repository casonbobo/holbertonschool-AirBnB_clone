#!/usr/bin/python3
"""This is a class struture for the base model
    for all classes for the AirBnB project"""
import uuid
from datetime import datetime


class BaseModel():
    """Base Model Class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Saves and updates the date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary representation of BaseModel"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__clas__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

    def __str__(self):
        """String representation function"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
