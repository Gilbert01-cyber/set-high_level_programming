#!/usr/bin/python3
"""Module that defines the Base class."""


class Base:
    """Base class that manages the id attribute for all future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
