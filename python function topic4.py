def check_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
def show_number():
    result=check_even(20)
    print(result)
show_number()

def add(a,b):
    return a+b
def result():
    answer=add(10,20)
    print("answer:", answer)
result()

def multiply(a,b):
    return a*b
def show_result():
    multi=multiply(3,6)
    print("multiply", multi)
show_result()

def check_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
def show_number():
    result=check_even(20)
    print(result)
show_number()

def calculate_total(price, tax):
    total=price+tax
    return total
def show_bill():
    shown=calculate_total(22,88)
    print(shown)
show_bill()

add = lambda a,b: a + b
print(add(10,20))

cube=lambda x: x*x*x
print(cube(4))

largest = lambda a, b: a if a > b else b
print(largest(2,3))



