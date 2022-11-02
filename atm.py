class Atm:
    __serial_no = 1
    # constructor
    def __init__(self):
        self.__pin = "123"
        self.__balance = 0
        self.sno = Atm.__serial_no
        Atm.__serial_no += 1
        # self.menu()

    def menu(self):
        user_input = input(
            """
				1.Enter 1 to create pin
				2.Enter 2 to deposit
				3.Enter 3 to withdraw
				4.Enter 4 to check balance
				5.Enter 5 to Account details
                6.Enter 6 to exit
				"""
        )
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            self.acc_details()
        else:
            print("bye")

    @staticmethod
    def get_serial_no():
        print(Atm.__serial_no)

    @staticmethod
    def set_serial_no(new):
        if type(new) == int:
            Atm.__serial_no = new
            print("Serial num set successfully!")
        else:
            print("Not allow!")

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print("Pin Changed!")
        else:
            print("Not Allow!")

    def get_balance(self):
        return self.__balance

    def pin_validation(self):
        temp_pin = input("Enter your pin:  ")
        if temp_pin == self.__pin:
            return True
        else:
            False

    def create_pin(self):
        self.__pin = input("Enter your pin:  ")
        print("Pin set successful:  ")

    def deposit(self):
        if self.pin_validation():
            amount = int(input("Enter amount to deposit:  "))
            self.__balance += amount
            print("Deposit operation successful!")
        else:
            print("Invalid pin!")

    def withdraw(self):
        if self.pin_validation():
            amount = int(input("Enter amount to withdraw:  "))
            if amount < self.__balance:
                self.__balance -= amount
                print("Withdraw operation successful!")
            else:
                print("Insufficient funds!")
        else:
            print("Invalid pin!")

    def check_balance(self):
        if self.pin_validation():
            print("Balance amount:  ", self.__balance)
        else:
            print("Invalid pin!")

    def acc_details(self):
        if self.pin_validation():
            print("Serial no :", self.sno)
            print("Pin code :", self.get_pin())
            print("Balance :", self.get_balance())
        else:
            print("Invalid pin!")


# sbi = Atm()
# aa = Atm()
Atm.get_serial_no()
Atm.set_serial_no(5)
Atm.get_serial_no()

# sbi.acc_details()

# print(sbi.get_serial_no())

# sbi2 = Atm()

# sbi2.acc_details()
# sbi.deposit()
# sbi.withdraw()
# sbi.check_balance()

# abi = Atm()

# abi.deposit()
# abi.withdraw()
# abi.check_balance()

# sbi.check_balance()
