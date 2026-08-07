class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        print(f" Product {self.name} price is {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total number of products are {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        print(f"Discounted price of product = price = {(price * discount / 100 )}")



p1 = Product("Phone", 40_000)
p2 = Product("Laptop", 50_000)
p3 = Product("Pen", 10) 
p1.get_info()
p1.calc_discount(50_000, 12)

