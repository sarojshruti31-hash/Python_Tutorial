# when deals with string
import json

py_obj = {
    "name": "Shruti",
    "isTeacher": True
}
json_str = json.dumps(py_obj)

print(type(json_str), json_str)



