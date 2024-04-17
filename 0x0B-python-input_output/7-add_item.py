#!/usr/bin/python3
"""
a module to do something
"""

import sys
import os
import json
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
l = sys.argv[1:]
a = []
for i in l:
    a.append(i)
if os.path.exists("add_item.json"):
    c = load_from_json_file ("add_item.json")
    c += a
    save_to_json_file(c, "add_item.json")

else:
    save_to_json_file(a, "add_item.json")
load_from_json_file ("add_item.json")
