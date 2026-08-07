# 1. Class Attributes belong to class --> common
# 2. Instance Attributes belongs to object --> unique
class Student:
    college_name = "ABC"

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
stu1 = Student("Rahul", 9.0)
print(Student.college_name)
print(stu1.name, stu1.cgpa)

    



