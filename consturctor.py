# Constructor --> is a function that helps to create object
# Syntax --> __init__Method (init is used to initialize our object) gets automatically called
# everytime , whenever an object is created.
# NO MULTIPLE CONSTURCTORS CAN BE CREATED and one __init__ method  can be used in a class


class Student:
      def __init__(self):  # [DEFAULT CONSTRUCTOR]
          print("object is constructed")

      def __init__(self, name, cgpa): # [ PARAMETERIZED CONSTRUCTOR] self --> current instance of class or showing reference to a current object
        self.name = name
        self.cgpa = cgpa
     
      def get__cgpa(self): 
          return self.cgpa


stu1 = Student("Shruti", 9.0)
stu2 = Student("Lucky", 9.1)
stu3 = Student("Tasneem", 9.2)
print(f"{stu1.name} has cgpa = {stu1.get__cgpa()}")


      






