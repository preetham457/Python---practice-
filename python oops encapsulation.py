class student:
    def __init__(self,name, age):
        self._name= name
        self._age= age
s1=student("preetham", 18)
print(s1._name)   
print(s1._age)


class student:
    def __init__(self,age):
        self.__age=age
    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        self.__age=new_age
s1=student(19)
print("old age:", s1.get_age())
s1.set_age(20)
print("new age:", s1.get_age())
       
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Invalid balance")


a1 = BankAccount(5000)

print("Balance:", a1.get_balance())

a1.set_balance(7000)
print("New balance:", a1.get_balance())

a1.set_balance(-100)

class student:
    def __init__(self,name):
        self. __name=name
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.__name=new_name
s1=student("preetham")
print("old name:", s1.get_name())    
s1.set_name("rahul")
print("new name:",s1.get_name())

class moble:
    def __init__(self,price):
        self. __price=price
    def get_price(self):
       return self.__price
    def set_name(self,new_price):
        self.__price=new_price
p1=moble("1000")
print("old price:",p1.get_price())

p1.set_name("5000")
print("new:", p1.get_price())


        
        