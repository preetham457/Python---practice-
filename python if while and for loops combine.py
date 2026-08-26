total = 0

for i in range(5):

    marks = int(input("Enter marks: "))

    while marks < 0 or marks > 100:
        print("Enter marks between 0 and 100")
        marks = int(input("Enter marks again: "))

    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    print("Grade:", grade)

    total = total + marks

average = total / 5

print("Total:", total)
print("Average:", average)
positive = 0
negative = 0
zero = 0
total = 0
largest = None

for i in range(10):
    num = int(input("Enter number: "))

    if num > 0:
        positive = positive + 1

    elif num < 0:
        negative = negative + 1

    else:
        zero = zero + 1

    total = total + num

    if largest is None or num > largest:
        largest = num

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)
print("Total:", total)
print("Largest:", largest)