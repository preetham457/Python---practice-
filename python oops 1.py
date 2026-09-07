class student:
    college="jnnce"
    def __init__(self, name, age):
        self.name=name
        self.age=age
s1= student("preetham",19)
s2=student("rahul", 18)
print(s1.name)
print(s1.age)
print(s1.college)
class Student:
    college = "JNNCE"

    @classmethod
    def show_college(cls):
        print(cls.college)

Student.show_college()
class Student:
    college = "JNNCE"

    @classmethod
    def change_college(cls, new_college):
        cls.college = new_college

Student.change_college("VTU")

print(Student.college)
class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

Student.change_school("XYZ School")

print(Student.school)
class Employee:
    company = "Google"

    @classmethod
    def change_company(cls, name):
        cls.company = name

Employee.change_company("Microsoft")

print(Employee.company)
class Person:
    country = "India"

    @classmethod
    def change_country(cls, new_country):
        cls.country = new_country

Person.change_country("Japan")

print(Person.country)