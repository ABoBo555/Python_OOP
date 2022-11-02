class Shape:
    # based on the passed argument method is overloaded
    def area(self, value1, value2=None):
        if value2 is None:
            print("This is circle", 3.14 * value1 * value1)
        else:
            print("This is square: ", value1 * value2)


s = Shape()
s2 = Shape()

s.area(15)
s2.area(4, 8)
