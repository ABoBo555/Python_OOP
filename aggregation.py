class citizen:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def show(self):
        print("Name: ", self.name)
        print("AGE: ", self.age)
        print("Gender: ", self.gender)
        print("City: ", self.address.city)
        print("Pin: ", self.address.pin)
        print("State: ", self.address.state)

    def edit_profile(self, name, age, gender, city, pin, state):
        self.name = name
        self.age = age
        self.gender = gender
        self.address.update_address(city, pin, state)


class Address:
    def __init__(self, city, pin, state):
        self.city = city
        self.pin = pin
        self.state = state

    def update_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pin = new_pin
        self.state = new_state
        print("This works")


add = Address("Yangon", 11071, "TGGN")
c1 = citizen("AAA", 22, "Male", add)
c1.show()
c1.edit_profile("BBB", 22, "Male", "MDY", "100000", "TWN")
c1.show()
print(add.city, add.pin, add.state)
