#!/usr/bin/python3
"""Module that defines a class inheriting from list."""


class MyList(list):
    """Represent a list with a method to print it sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
