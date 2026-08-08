class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, cgpa):
        self.cgpa = cgpa

class TeacherAssistant(Teacher, Student):
    def __init__(self, name, salary, cgpa):
        super().__init__(salary)
        Student.__init__(self, cgpa)
        self.name = name

ta1 = TeacherAssistant("Shruti", 200_00, 9.0)
print(ta1.name, ta1.salary, ta1.cgpa)

