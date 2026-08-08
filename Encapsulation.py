# Wrapping data & functions into single unit
# data hidhing is done using encapsulation
# 1. public
# 2. protected ( class + subclasses)
# 3. private --> inside the class  [to data be accessed priavtely to official users we use getters and setters]
class BankAccount:
    def __init__(self, name, balance):
        self.name = name   # public 
        self.__balance = balance  # pivate

    def get_balance(self):  # getters
        return self.__balance

    def set_balance(self, newBalance):
        self.__balance = newBalance


acc1 = BankAccount("Shruti", 100_000)  # setters
acc1.set_balance(200_000)
print(acc1.name, acc1._BankAccount__balance)    # without using getters





