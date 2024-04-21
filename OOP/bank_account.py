class BankAccount:
    def __init__(self,account_number,balance):
        self._account_number = account_number #protected attribute
        self.__balance = balance #private attribute
    
    # getter method for private attribute
    def get_balance(self):
        return self.__balance
    # setter method for the private attribute
    def set_balance(self,balance):
        if balance >=0:
            self.__balance = balance
        else:
            print("Invalid balance")

    #public method that uses the private attribute

    def depposit(self,amount):
        if amount>0:
            self.__balance += amount
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if amount>0:
            self.__balance -= amount
        else:
            print("Invalid withdrawal amount")

# testing the encapsulation
account = BankAccount("123456",1000)
