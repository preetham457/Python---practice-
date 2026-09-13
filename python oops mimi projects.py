class bankaccount:
    def __init__(self,name,balance):
        self .name=name
        self .balance=balance
    def show_balance(self):
        print("name:", self.name)
        print("balance:", self.balance)
    def deposite(self,amount):  
        self.balance=self.balance  + amount
b1=bankaccount("preetham",1000)
b1.show_balance()  
b1.deposite(200)
b1.show_balance

class bankaccount:
    def __init__(self,name,balance):
        self .name=name
        self .balance=balance
    def show_balance(self):
        print("name:", self.name)
        print("balance:", self.balance)
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
b1=bankaccount("preetham",1000)
b1.show_balance() 
b1.withdraw(300)
from abc import ABC, abstractmethod

# ABSTRACTION
class BankAccount(ABC):

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance     # ENCAPSULATION

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        self.__balance = amount

    @abstractmethod
    def account_type(self):
        pass


# INHERITANCE
class SavingsAccount(BankAccount):

    def account_type(self):
        print("Savings Account")

    # POLYMORPHISM
    def show_details(self):
        print("Name:", self.name)
        print("Balance:", self.get_balance())
        print("Type: Savings Account")


class CurrentAccount(BankAccount):

    def account_type(self):
        print("Current Account")

    # POLYMORPHISM
    def show_details(self):
        print("Name:", self.name)
        print("Balance:", self.get_balance())
        print("Type: Current Account")


# Objects
s1 = SavingsAccount("Preetham", 5000)
c1 = CurrentAccount("Rahul", 8000)

s1.show_details()
s1.account_type()

print()

c1.show_details()
c1.account_type()


from abc import ABC, abstractmethod

# ABSTRACTION
class Student(ABC):

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks       # ENCAPSULATION

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks

    @abstractmethod
    def course(self):
        pass


# INHERITANCE
class DataScienceStudent(Student):

    # POLYMORPHISM
    def course(self):
        print("Course: Data Science")


class AIStudent(Student):

    # POLYMORPHISM
    def course(self):
        print("Course: Artificial Intelligence")


# Objects
s1 = DataScienceStudent("Preetham", 85)
s2 = AIStudent("Rahul", 90)

# Calling methods
print("Name:", s1.name)
s1.course()
print("Marks:", s1.get_marks())

print()

print("Name:", s2.name)
s2.course()
print("Marks:", s2.get_marks())
       
                    