class A:
    def __init__(self):
        self.var = 100

    def display1(self, var):
        print("class A:", self.var)


class B(A):
    def display2(self, var):
        print("class B: ", self.var)


b = B()
b.display1(200)
# tho it pass 200 in var it is not used and
# self.var from __init__ is used thus why
