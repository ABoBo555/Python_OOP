# Method Reservation Order
class Product:
    def buy(self):
        print("Buying a product.")


class Phone:
    def __init__(self, price, brand, camera):
        # print("Inside Phone __init__")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone.")


class Smartphone(Product, Phone):
    pass


sm = Smartphone(100000, "Oppo", "1000px")
sm.buy()


# Parent ---> Child
# Product ---> Smartphone
# Phone ---> Smartphone


# Product     Phone     ---> parent
#    |         |
#    Smartphone()       ---> child
