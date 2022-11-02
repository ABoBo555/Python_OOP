class Phone:
    def __init__(self, price, brand, camera):
        print("This is parent Initializer")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Hierarchical Inheritance.", self)


class Smartphone(Phone):
    pass


class Featurephone(Phone):
    pass


sm = Phone(120000, "vivo", "100px")
fp = Phone(150000, "oppo", "100px")


sm.buy()
fp.buy()
