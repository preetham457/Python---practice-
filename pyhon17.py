marks=int(input("enter youe marks:"))
if marks>=90:
    print("pass")
else:
    print("fail")


num1=int(input("enter frist number:"))
num2=int(input("enter second number:"))
print("addition:", num1+num2)
print("subtraction:", num1-num2)
print("multiplication:", num1*num2)
print("division:", num1/num2)


age=int(input("enter yourn age:"))
if age>=18:
    print("your and you can vote")
else:
    print("your and you can not vote")

num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))
if num1>num2:
    print(num1,"is greater thaan larger")
elif num2>num3:
    print(num2,"is greater than larger")
else:
    print(num3,"is greater than larger")



num=int(input("enter a number:"))
if num>=90:
    print("pass")
elif num>=60:
    print("average")
elif num>=35:
    print("fali")

num=int(input("enter a number:"))
for i in range(1,11):
    print(num*i)




for i in range(1,21):
    if i % 2 == 0:
        print(i)
    
                
count=0
for i in range(5):
    num=int(input("enter number:"))
    if num%2==0:
        count = count+1
print("even number:",count)


for i in range(5):
    num = int(input("Enter number: "))

    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")




total=0

for i in range(5):
    num=int(input("enter the number "))
    if num>0:
        total=total+num
print("total of positive number:", total)

number=int(input("enter the number:"))

if number%2==0:
       print("even")
else:
       print("odd")



