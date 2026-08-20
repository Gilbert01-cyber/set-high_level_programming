#!/usr/bin/python3
"""Module for saving an object to a text file using JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file, using a JSON representation."""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f) 
