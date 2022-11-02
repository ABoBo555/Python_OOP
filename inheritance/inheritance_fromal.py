class Phone:
    # def __init__(self,price,brand,camera):
    #     self.price = price
    #     self.brand = brand
    #     self.camera = camera

    def show_detail(self):
        print("Parent class show_details.")

    def find_id(self):
        print("Parent class find id.")


class Smartphone(Phone):  # inherit from Phone class
    def call(self):
        print("Child smartphone class call fun.")

    def register(self):
        print("Child smartphone class reg fun.")


# Child class inherit other two class form parent
s1 = Smartphone()
s1.call()
s1.register()
s1.find_id()
s1.show_detail()

s1 = Phone()
s1.call()  # parent class obj calling child's method => raise error
# (inheritance is one way interaction) only child can access parent attributes
