from abc import ABC, abstractmethod


# ABSTRACTION
class Hospital(ABC):

    def __init__(self, name, fees):
        self.name = name
        self.__fees = fees       # ENCAPSULATION

    def get_fees(self):
        return self.__fees

    def set_fees(self, fees):
        self.__fees = fees

    @abstractmethod
    def treatment(self):
        pass


# INHERITANCE
class Doctor(Hospital):

    # POLYMORPHISM
    def treatment(self):
        print("Doctor gives treatment")

    def details(self):
        print("Doctor Name:", self.name)
        print("Fees:", self.get_fees())


class Patient(Hospital):

    # POLYMORPHISM
    def treatment(self):
        print("Patient receives treatment")

    def details(self):
        print("Patient Name:", self.name)
        print("Fees:", self.get_fees())


# Objects
d1 = Doctor("Dr. Ravi", 500)
p1 = Patient("Preetham", 300)


# Doctor
d1.details()
d1.treatment()

print()

# Patient
p1.details()
p1.treatment()