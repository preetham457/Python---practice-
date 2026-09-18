class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter age: "))

    if age < 0:
        raise InvalidAgeError("Age cannot be negative")

    print("Age:", age)

except InvalidAgeError as e:
    print("Error:", e)
class InvalidMarksError(Exception):
    pass


try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")

    print("Marks:", marks)

except InvalidMarksError as e:
    print("Error:", e)

