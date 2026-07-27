#!/usr/bin/python3
"""Module that defines the MyInt class."""


class MyInt(int):
    """Represent an integer with inverted == and != operators."""

    def __eq__(self, value):
        """Return the inverted equality comparison."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Return the inverted inequality comparison."""
        return super().__eq__(value)
