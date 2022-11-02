# with super() child class is only callable
# parent's method and parent's initializer not properties


class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")


class Smartphone(Phone):
    def buy(self):
        print("Buying a smartphonen")
        super().buy()  # super() fun is only callable in child class
        # super().price # this will also raise error can't access parent properties


sm = Smartphone(100000, "Vivo", "1000px")
sm.buy()

# sm.super().buy()
# this will raise error since super() is called outside class
