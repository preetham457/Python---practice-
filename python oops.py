class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
a1=bankaccount("preethahm",1000)
a2=bankaccount("rahul",2000)
print(a1.name,a1.balance)
print(a2.name,a2.balance)
   

class student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name, "is studying")
s1=student("preetham", 19)
s1.display()

class rectangle:
    def __init__(self, length,width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length*self.width ,"rectangle")
r1=rectangle(77,99)
r1.area()
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount


a1 = BankAccount("Preetham", 5000)

print("Name:", a1.name)
print("Starting balance:", a1.balance)

a1.deposit(2000)

print("Deposit: 2000")
print("Final balance:", a1.balance)
