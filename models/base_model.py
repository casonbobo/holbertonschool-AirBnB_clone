#!/usr/bin/python3
"""This is a class struture for the base model
    for all classes for the AirBnB project"""
import uuid
from datetime import datetime


class BaseModel():
    """Base Model Class"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            if '__class__' in kwargs:
                kwargs.pop('__class__')
            for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """Saves and updates the date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Dictionary representation of BaseModel"""
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        """String representation function"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))
