class Phone:
    def __init__(self, price, brand, camera):
        print("Inside Phone __init__")
        self.price = price
        self.brand = brand
        self.camera = camera


class Smartphone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        print("First reach here.")
        self.os = os
        self.ram = ram
        super().__init__(price, brand, camera)
        print("Inside smartphone __init__")


sm = Smartphone(150000, "Vivo", "1000px", "Android", 2)
print(sm.os)  # os var is assigned in child __init__
print(sm.brand)  # brand var is assigned in parent __init__
