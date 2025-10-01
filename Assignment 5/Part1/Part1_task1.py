class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number   # private attribute
        self.__balance = balance                 # private attribute

    # deposit method
    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print("Deposit successful. New Balance:", self.__balance)

    # withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
            print("Withdraw successful. New Balance:", self.__balance)
        else:
            print("Not enough balance!")

    # balance check method
    def get_balance(self):
        return self.__balance


acc1 = BankAccount("ACC001", 0)

# User se input lena
deposit_amount = int(input("Enter amount to deposit: "))
acc1.deposit(deposit_amount)

withdraw_amount = int(input("Enter amount to withdraw: "))
acc1.withdraw(withdraw_amount)

print("Final Balance:", acc1.get_balance())