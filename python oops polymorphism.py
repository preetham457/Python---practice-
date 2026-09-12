class dog:
    def sound(self):
        print("dog barks")
class cat:
    def sound(self):
        print("cat barks")
d1=dog()
c1=cat()
d1.sound()
c1.sound()


class animal:
    def sound(self):
        print("the kinhg")
class dog:
    def sound(self):
        print("dog barks")
class cat:
    def sound(self):
        print("cat meows")
a1=animal()
d1=dog()
c1=cat()
a1.sound()
d1.sound()
c1.sound()

class payment:
    def pay(self):
        print("the amount")
class upt(payment):
    def pay(self):
        print("payment through")
class card(payment):
    def pay(self):
        print("payment through card")
p1=payment()
u1=upt()
c1= card()
p1.pay()
u1.pay()
c1.pay()
class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


class Cow:
    def sound(self):
        print("Cow moos")


d1 = Dog()
c1 = Cat()
c2 = Cow()

animals = [d1, c1, c2]

for animal in animals:
    animal.sound()


    