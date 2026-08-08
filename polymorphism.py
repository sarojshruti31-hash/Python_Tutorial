# Poly -> many and morphism -> forms
# different function -> same name
# eg: OPERATOR OVERLOADING
# 1. FUNCTION OVERRIDING  -> redefinimg parent class  functions in child class
class Employee:
    def get_designation(self):
        print("Designation = Employee")

class Teacher(Employee):
    def get_designation(self):
            print("Designation = Teacher")

t1 = Teacher()
t1.get_designation()
    

# 2. DUCK TYPING
class Teacher:
    def get_designation(self):
        print("Designation = Teacher")

class Accountant(Employee):
    def get_designation(self):
            print("Designation = Accountant")

t1 = Teacher()
t1.get_designation()

acc1 = Accountant()
acc1.get_designation()

