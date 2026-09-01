def calculate_marks(a, b, c):

    sum = a + b + c
    average = sum / 3

    return sum, average


sum, average = calculate_marks(80, 70, 90)

print("Total:", sum)
print("Average:", average)

def calculate_salary(salary, experce):
    if experce>=5:
        bons=salary*10/100
    else:
        bons=salary*5/100
    final_salary = salary + bons

    print("Final salary:", final_salary)


salary = int(input("Enter salary: "))
experience = int(input("Enter experience in years: "))

calculate_salary(salary, experience)

def calculate_discount(price):

    if price >= 1000:
        discount = price * 10 / 100
        return discount
    else:
        discount = price * 5 / 100
        return discount

discount = calculate_discount(1000)

print("Discount:", discount)


def find_largest(a,b):
   if a>b:
       return a
   else:
       return b
largest=find_largest(2,1)
print("largest:",largest )

def calculate(a,b):
   sum=a+b
   diffence=a-b
   return sum,diffence
sum, difference=calculate(20,8)
print("sum:",sum)
print("diference:",difference)

      
def calculate_marks(a, b, c):

    sum = a + b + c
    average = sum / 3

    return sum, average


sum, average = calculate_marks(80, 70, 90)

print("Total:", sum)
print("Average:", average)


def check_result(marks):
    if marks>35:
        return "pass"
    else:
        return "fali"
result=check_result(60)
print(result)   




    


