class Phone:
    def __init__(self, price, brand, camera):
        print("parent Initializer is constructed.")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("This is Parent class")


class Smartphone(Phone):
    def buy(self):
        print("This is Child class")


# both child and parent classes has a same function named buy()
# if a child obj is created , buy() method is called it overrides the parent's fun

s = Smartphone(120000, "Vivo", "1200px")
s.buy()  # child

s2 = Phone(210000, "Oppo", "1200px")
s2.buy()  # parent
