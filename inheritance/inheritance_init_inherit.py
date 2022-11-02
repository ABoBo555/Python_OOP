# initializer inheriting
# child can inherit only public attributes and initializer
class Phone:
    def __init__(self, price, brand, camera):
        print("This is parent Initializer")
        self.price = price
        self.brand = brand
        self.camera = camera
        self.__private_var = "Private var can't access by child"


class Smartphone(Phone):  # inherit from Phone class
    # no initializer is this class
    def info(self):
        print("This is smartphone class.")


# 1. a class find initializer in its class
# 2. when it doesn't find , it go to parent class and assign value in that parent's initializer
# 3. so, parent initializer is printed
sm = Smartphone(100000, "IPhone", "1000px")
print("Smartphone info: ", sm.price, sm.brand, sm.camera)

try:
    if sm.__private_var:
        print("Private var can access")

except AttributeError:
    print("Private var can't access by child")
