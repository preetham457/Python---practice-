class bankacount:
    def __init__(self, name,balance):
        self.name=name
        self.__balance=balance
        
    def deposite(self,amount):
        self.__balance+=amount
        print("Deposite", amount)
        
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("withdrawm:", amount)
        else:
            print("insufficient balance")
    def show_balance(self):
        print("balance:",self.__balance) 
        
class savingaccount(bankacount):
    def calculate_interest(self):
        print("saving account interest added")
        
        
class currentaccount(bankacount):
    def   withdraw(self, amount):
            print ("current account withdraw")
            super() .withdraw(amount)

s=savingaccount("preetham", 5000)
c=currentaccount("rahul", 3000)

s.deposite(1000)
s.show_balance()

c.withdraw(500)
c.show_balance()
    


    
    
                             