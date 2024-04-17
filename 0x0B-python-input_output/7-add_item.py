#!/usr/bin/python3
"""
a module to do something
"""


import sys
import json
__import__("5-save_to_json_file").save_to_json_file
__import__("6-load_from_json_file").load_from_json_file
a = sys.argv[1:]
with open("add_item.json", "w", encoding="utf-8") as f:
    json.dump(a, f)
