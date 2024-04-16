#!/usr/bin/python3
"""
contain a function
"""


def load_from_json_file(filename):
    """
    this is a function
    """
    import json
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
