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
        return {'id': self.id, 'width': self.__width, 'height':
                self.__height, 'x': self.__x, 'y': self.__y}

    def __str__(self):
        """String representation function"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
