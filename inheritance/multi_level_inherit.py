class product:
    def review(self):
        print("Product customer review")


class Phone(product):
    def __init__(self, price, brand, camera):
        print("Inside Phone __init__")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Phone class inside fun buy()")


class Smartphone(Phone):
    pass


sm = Smartphone(150000, "Vivo", "1000px")
p = Phone(120000, "Iphone", "1100px")

sm.buy()
sm.review()
p.review()
