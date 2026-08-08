#2. to write from json file use json.dump
import json

data = {
    "name": "Shraddha",
    "isTeacher": True,
    "age": 21
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)
