#!/usr/bin/python3
"""Defines MagicClass, reverse-engineered from bytecode."""
import math


class MagicClass:
    """Represents a shape with a radius."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius: The radius of the shape.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area based on the radius."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Return the circumference based on the radius."""
        return 2 * math.pi * self.__radius
