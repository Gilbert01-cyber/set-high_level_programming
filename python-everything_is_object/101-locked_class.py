#!/usr/bin/python3
"""Module that defines a class with restricted attribute creation."""


class LockedClass:
    """Represent a class that prevents dynamic attribute creation.

    The only attribute allowed to be set is `first_name`.
    """

    __slots__ = ['first_name']
