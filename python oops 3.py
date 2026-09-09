class Student:
    course = "Data Science"

    @classmethod
    def change_course(cls, new_course):
        cls.course = new_course

Student.change_course("Cyber Security")

print("Course:", Student.course)
class Mobile:
    brand = "Samsung"

    @classmethod
    def change_brand(cls, new_brand):
        cls.brand = new_brand

Mobile.change_brand("Motorola")

print("Brand:", Mobile.brand)
class Game:
    level = 1

    @classmethod
    def change_level(cls, new_level):
        cls.level = new_level

Game.change_level(5)

print("Level:", Game.level)
class College:
    university = "VTU"

    @classmethod
    def change_university(cls, new_university):
        cls.university = new_university

College.change_university("Bangalore University")

print("University:", College.university)