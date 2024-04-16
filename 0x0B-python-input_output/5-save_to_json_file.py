#!/usr/bin/python3
"""
conatain a function
"""


def save_to_json_file(my_obj, filename):
    """
    a function to make an action
    """
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
