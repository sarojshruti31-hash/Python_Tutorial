# 1. instance (1st parameter[self] and access the class and instance attributes)
class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

l1.get_info()

# 2. class method (can only access class attributes not instace attributes)
# Syntax --> (cls)
class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod  # decorator
    def get_storage_type(cls): # Class method
        print(f"storage type = {cls.storage_type}")


    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

l1 = Laptop("16gb", "512gb")
Laptop.get_storage_type()

# 3 . static method
# NO COMPULSORY PARAMETER [i.e no class & no instance]
# cannot access instance and class attributes
class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod  # decorator
    def get_storage_type(cls): # Class method
        print(f"storage type = {cls.storage_type}")


    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @staticmethod  #decorator
    def calc_discount(price, discount):
     final_price = price - (discount * price / 100) 
     print(f"Discounted Price = {final_price}")

l1 = Laptop("16gb", "512gb")
l1.calc_discount(40_000, 10)




