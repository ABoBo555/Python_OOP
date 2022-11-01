class Atm:
    # constructor
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input(
            """
				1.Enter 1 to create pin
				2.Enter 2 to deposit
				3.Enter 3 to withdraw
				4.Enter 4 to check balance
				5.Enter 5 to exit
				"""
        )
        if user_input == "1":
            self.create_pin()
        # elif user_input == "2":
        #     self.deposit()
        # elif user_input == "3":
        #     self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("bye")

    def pin_validation(self):
        temp_pin = input("Enter your pin:  ")
        if temp_pin == self.pin:
            return True
        else:
            False

    def create_pin(self):
        self.pin = input("Enter your pin:  ")
        print("Pin set successful:  ")

    def deposit(self):
        if self.pin_validation():
            amount = int(input("Enter amount to deposit:  "))
            self.balance += amount
            print("Deposit operation successful!")
        else:
            print("Invalid pin!")

    def withdraw(self):
        if self.pin_validation():
            amount = int(input("Enter amount to withdraw:  "))
            if amount < self.balance:
                self.balance -= amount
                print("Withdraw operation successful!")
            else:
                print("Insufficient funds!")
        else:
            print("Invalid pin!")

    def check_balance(self):
        if self.pin_validation():
            print("Balance amount:  ", self.balance)
        else:
            print("Invalid pin!")


sbi = Atm()

sbi.deposit()
sbi.withdraw()
sbi.check_balance()

# abi = Atm()

# abi.deposit()
# abi.withdraw()
# abi.check_balance()

# sbi.check_balance()
