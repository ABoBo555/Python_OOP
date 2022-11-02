class Product:
    def __init__(self, price, brand, camera):
        print("Inside Product __init__")
        self.price = price
        self.brand = brand
        self.camera = camera

    def review(self):
        print("Product customer review")


class Phone:
    # def __init__(self, price, brand, camera):
    #     print("Inside Phone __init__")
    #     self.price = price
    #     self.brand = brand
    #     self.camera = camera

    def buy(self):
        print("Buying a phone.")


# when a smartphone inherit from two parent class
# child find __init__ in its own class
# if doesn't find go to first position parent class here <Phone class> is in first position,
# if both child and first position class don't have __init__ it find the 2nd position class, so on and so forth


class Smartphone(Phone, Product):
    pass


sm = Smartphone(120000, "vivo", "1000px")
sm.buy()
sm.review()
