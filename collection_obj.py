class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("Name :", self.name, " Age :", self.age)


s1 = Student("A", 12)
s2 = Student("B", 15)

L = [s1, s2]

for i in L:
    i.intro()
