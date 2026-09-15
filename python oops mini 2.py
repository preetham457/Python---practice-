from abc import ABC, abstractmethod
class bankaccount(ABC):
    def __init__(self,name,blance):
        self.name=name
        self.__balance=blance
    def get_balance(self):
        return self.__balance
    def set_balance(self,blance):
        self.__balance=blance
        @abstractmethod
        def acconut_type(self):
            pass
class SavingsAccount(bankaccount):
    def account_type(self): 
        print("this my savingsaccount")
    def detailst(self):
        print("name:", self.name)
        print("balnce:", self.get_balance())
class  currentAccount(bankaccount):
    def account_type(self):
        print("the is my currentaccount")
    def detailst(self):
        print("name:", self.name)
        print("balance:", self.get_balance())
s1=SavingsAccount("Preetham" ,1000)
c1=currentAccount("rahul", 1999)
s1.detailst()
s1.account_type()

print()

c1.detailst()
c1.account_type()
