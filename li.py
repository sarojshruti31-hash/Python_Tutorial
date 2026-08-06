# List is a MUTABLE sequence of values
marks = [99, 98, 95, 89]
print(marks[0])
print(len(marks))

# as it is mutable unlike str, we can update values
marks = [99, 98, 95, 89]
marks[2] = 78
print(marks)
print(type(marks))

# Slicing on lists ( create sublists)
marks = [88, 98, 56, 90, 87, "abc", 100.0]
print(marks[0:5])
print(marks[-5:-2])




