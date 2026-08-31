def greet(name):
    print("hello,", name)
greet("preetham")

def add(a ,b):
    print("sum:", a+b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
add(num1,num2)

def student(name , age, branch):
    print(name, age , branch)
student("preetham", 18,"dcs")

def check_number(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
check_number(6)


def calculate_bill(price, quantity):

    total = price * quantity

    print("Total bill:", total)


calculate_bill(2, 3)