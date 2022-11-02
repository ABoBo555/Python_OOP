class Parent:
    def __init__(self):
        self.num = 100


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var = 200

    def show(self):
        print(self.var)
        print(
            "Accessing num inside child class", self.num
        )  # access parent properties inside child class using self


c = Child()
print("Accessing num outside child class", c.num)
c.show()
