#!/usr/bin/python3
"""Module for returning the dict description of an object."""


def class_to_json(obj):
    """Return the dictionary description of a simple object."""
    return obj.__dict__
