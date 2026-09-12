from abc import  ABC, abstractmethod
class vehical (ABC):



    @abstractmethod
    def start(self):
        pass
class car(vehical):
    def start(self):
        print("good car")

c1=car()
c1.start()


from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def login(self):
        pass


class SBI(Bank):
    def login(self):
        print("Login using SBI app")


class HDFC(Bank):
    def login(self):
        print("Login using HDFC app")


s1 = SBI()
h1 = HDFC()

s1.login()
h1.login()
from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def interest(self):
        pass


class SBI(Bank):

    def interest(self):
        print("SBI interest is 7%")


class HDFC(Bank):

    def interest(self):
        print("HDFC interest is 8%")


s1 = SBI()
h1 = HDFC()

s1.interest()
h1.interest()
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment through UPI")


class Card(Payment):

    def pay(self):
        print("Payment through Card")


p1 = UPI()
p2 = Card()

payments = [p1, p2]

for payment in payments:
    payment.pay()