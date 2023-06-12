#!/usr/bin/python3
"""
This is the class for storing the files
after window close or program shut down
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode="r",encoding='utf-8') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    obj = eval(obj_dict['__class__'])(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
