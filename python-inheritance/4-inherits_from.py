#!/usr/bin/python3
"""Module that defines a function to check strict inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj's class inherited from a_class (not exact)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
