class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num


class Child(Parent):
    def __init__(self, var, num):
        self.__var = var
        super().__init__(num)

    def get_var(self):
        return self.__var


c = Child(100, 200)
print(c.get_var())
print(c.get_num())
