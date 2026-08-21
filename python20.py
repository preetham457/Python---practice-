
count = 0

for i in range(5):
    num = int(input("Enter number: "))

    if num % 2 != 0:
        count = count + 1

print("Odd numbers:", count)


count = 0

for i in range(5):
    num = int(input("Enter number: "))

    if num<0:
        count = count + 1

print("negative number:", count)



num=int(input("enter the number:"))
for i in range(1,11):
    print(num,"X" , i,"=", num*1)


num = int(input("Enter number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse:", reverse)


num=int(input("enter the number:"))
total=0
while num>0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of digits:", total)




num=int(input("enter the number:"))
count = 0

while num > 0:
    num = num // 10
    count = count + 1

print("Number of digits:", count)



num = int(input("Enter number: "))
count = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        count = count + 1

    num = num // 10

print("Even digits:", count)
