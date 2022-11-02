class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        print(self.__num)


class Child:
    def __init__(self, var, num):
        self.__var = var

    def get_var(self):
        print(self.__var)


c = Child("one", 1)
c.get_var()

try:
    if c.get_num():
        print("All good.")

except AttributeError:
    print("Since parent initializer is not called self.__num is not set")
