class Parent:
    def show(self):
        print("This is Parent")


class Child(Parent):
    pass


c1 = Child()
c1.show()

class animal:
    def show(self):
        print("animal is eating")
class dog(animal):
        pass
d1 = dog()
d1.show()


class animal:
    def __init__(self,name):
          self.name=name
    def show_name(self):
         print("animal:", self.name)
class dog(animal):
     pass
d1=dog("tommy")
d1.show_name

class student:
     def __init__(self,name,age):
          self.name=name
          self.age=age
     def show_name(self):
          print(self.name ,self.age)
class collegestudent(student):
     pass
p1=student("preetham",19)
p1.show_name()
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class CollegeStudent(Student):
    def __init__(self, name, age, branch):
        super().__init__(name, age)
        self.branch = branch


p1 = CollegeStudent("Preetham", 19, "Data Science")
print(p1.name)
print(p1.branch)

class person:
    def __init__(self,name):
         self.name=name
    def show_name(self):
         print("name:", self.name)
class student(person):
     def __init__(self, name,course):
          super().__init__(name)
          self.course=course
     def show_course(self):
          print("course:", self.course)
d1 = student("Preetham", "Data Science")

d1.show_name()
d1.show_course()