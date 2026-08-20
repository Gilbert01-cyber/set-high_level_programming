#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON export."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the instance.

        If attrs is a list of strings, only attributes whose names
        are in that list are included. Otherwise, all attributes
        are included.
        """
        if isinstance(attrs, list) and all(isinstance(a, str)
                                            for a in attrs):
            return {k: v for k, v in self.__dict__.items()
                    if k in attrs}
        return self.__dict__
