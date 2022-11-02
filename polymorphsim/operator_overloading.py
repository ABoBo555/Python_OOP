class Fraction:
    def __init__(self, num, dem):
        self.num = num
        self.dem = dem

    def __str__(self):
        return "{}/{}".format(self.num, self.dem)

    #   This __add__ fun over loaded the '+' operator, so that is operator overloading
    def __add__(self, other):
        temp_num = (self.num * other.dem) + (other.num * self.dem)
        temp_dem = self.dem * other.dem
        return "{}/{}".format(temp_num, temp_dem)


f = Fraction(133, 3)
print(f + f)
