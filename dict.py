# has key:value pairs which KEY IS ALWAYS UNIQUE
info = {
    "name": "Shruti",
    "cgpa": 9.0,
    "subjects": ["maths", "science"], 
    3.14: "PI"
    }
print(info)
print(type(info))
print(info["name"])

# Dictionary are MUTABLE
info["cgpa"] = 9.5
print(info)

# Dictinary are UNORDERED