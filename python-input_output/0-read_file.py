#!/usr/bin/python3
"""Module that defines a function to read a UTF8 text file and print it."""


def read_file(filename=""):
    """Read a text file (UTF8) and print its content to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
