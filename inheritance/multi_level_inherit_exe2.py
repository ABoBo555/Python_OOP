class A:
    def m1(self):
        return 20


class B(A):
    def m1(self):
        val = super().m1() + 30
        return val


class C(B):
    def m1(self):
        val = (
            self.m1() + 20
        )  # here self is obj3 and it recursively call itself thus why RecurssionError occur
        return val


obj3 = C()
print(obj3.m1())
