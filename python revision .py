
name=[10,20,30,40,50]
print(name[2])
name=[10,20,30,40,50]
name.append(60)
print(name)

i = 1

while i <= 10:
    if i == 5:
        i = i + 1
        continue

    print(i)
    i = i + 1

num=int(input("enter the number:"))

if num>0:
    print("postive")
elif num<0:
    print("negative")
else:
    print("zero")
for i in range(1,11):
    print("number:", i)
i=1
while i<=10:
    print(i)
    i=i+1
i=1
while i<=10:
    if i==5:
        break
    print(i)
    i=i+1
i = 1

while i <= 10:
    if i == 5:
        continue

    print(i)
    i = i + 1

name=[10,20,30,40,50]
a=[2]
print(a)

x = 10

def change():
    global x
    x = 20

change()

print(x)
    
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Preetham", age=18, branch="Data Science")
def count(n):
    if n > 5:
        return

    print(n)
    count(n + 1)

count(1)

def add(a, b):
    return a + b

add = lambda a, b: a + b

print(add(10, 20))

def check_result(marks):
    result = lambda m: "Pass" if m >= 35 else "Fail"
    return result(marks)

print(check_result(75))
print(check_result(25))