#!/usr/bin/python3
"""Contains the Base class definition"""
import json
import csv


class Base:
    """Defines the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns: the json string representation of an obj(dictionary)"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
           list_objs: a list of instances who inherits of Base

        Returns:
           None
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"

        with open(filename, 'w') as f:
            list_dict = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(list_dict))

    def from_json_string(json_string):
        """Returns: the list of the JSON string representation json_string

        Args:
           json_string: a string representing a list of dictionaries
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        else:
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns: a list of instances"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as f:
                content = f.read()
                list_dict = cls.from_json_string(content)
                instances = [cls.create(**d) for d in list_dict]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.
        Args:
           list_objs (list): A list of inherited Base instances.

        Returns:
           None
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as f:
            if list_objs is None or not list_objs:
                csv.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file"""
        filename = f"{cls.__name__}.csv"

        try:
            with open(filename, 'r', newline='') as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dict = csv.DictReader(f, fieldnames=fieldnames)
                list_dict = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dict]
                return [cls.create(**d) for d in list_dict]
        except FileNotFoundError:
            return []
