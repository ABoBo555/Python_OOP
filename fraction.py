# This file has create a new data fraction and its blueprint
# can perform +,-,*,/ operations with fraction
# eg. 2/3 + 2/3 => 12/9 => 4/3

from math import gcd, floor, ceil


class Fraction:
    def __init__(self, num, dem):
        self.num = num
        self.dem = dem
        self.num, self.dem = self.simplify_frac(self.num, self.dem)

    def __str__(self):
        return "{}/{}".format(self.num, self.dem)

    def __add__(self, other):
        temp_num = (self.num * other.dem) + (other.num * self.dem)
        temp_dem = self.dem * other.dem
        temp_num, temp_dem = self.simplify_frac(temp_num, temp_dem)
        return "{}/{}".format(temp_num, temp_dem)

    def __sub__(self, other):
        temp_num = (self.num * other.dem) - (other.num * self.dem)
        temp_dem = self.dem * other.dem
        temp_num, temp_dem = self.simplify_frac(temp_num, temp_dem)
        return "{}/{}".format(temp_num, temp_dem)

    def __mul__(self, other):
        temp_num = self.num * other.num
        temp_dem = self.dem * other.dem
        temp_num, temp_dem = self.simplify_frac(temp_num, temp_dem)
        return "{}/{}".format(temp_num, temp_dem)

    def __truediv__(self, other):
        temp_num = self.num * other.dem
        temp_dem = self.dem * other.num
        temp_num, temp_dem = self.simplify_frac(temp_num, temp_dem)
        return "{}/{}".format(temp_num, temp_dem)

    def decimal_form(self):
        print(self.num / self.dem)

    def floor(self):
        print(floor(self.num / self.dem))

    def ceil(self):
        print(ceil(self.num / self.dem))

    @staticmethod
    def simplify_frac(num_value, dem_value):
        gcd_value = gcd(num_value, dem_value)
        temp_num = num_value // gcd_value
        temp_dem = dem_value // gcd_value
        return temp_num, temp_dem


f = Fraction(2, 3)
# g = Fraction(6, 9)
# f.decimal_form()
# f.ceil()
# f.floor()
# print(g) #simplify original frac in init
print(f + f)
