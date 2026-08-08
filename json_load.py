# deals with files 
#1. to read data from json file use json.dump
import json
with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(type(py_obj), py_obj)


