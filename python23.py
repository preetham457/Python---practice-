num = int(input("Enter number: "))

count = 0

while num > 0:
    digit = num % 10

    if digit == 0:
        count = count + 1

    num = num // 10

print("Number of zeros:", count)

num = int(input("Enter number: "))
count=0
while num>0:
    digit=num%10
    if digit>5:
        count=count+1
    num=num//10

print("greater than 5:", count)

num = int(input("Enter number: "))

count = 0

while num > 0:

    digit = num % 10

    if digit < 5:
        count = count + 1

    num = num // 10

print("Digits less than 5:", count)


num = int(input("Enter number: "))
total=0
while num>0:
    digit=num%10

    if digit>5:
        total = total+digit
    num=num//10
  
print("sum digit greater than:",total )
    
num = int(input("Enter number: "))
total=0
while num>0:
    digit=num%10
    if digit%2==0:
        total=total+digit
    num=num//10
print("sum of even digits:",total)


 
num = int(input("Enter number: "))
product=1
while num>0:
    digit=num%10
    if digit%2==0:
        product=product*digit
    num=num//10
print("product of even digits:",product)


 
num = int(input("Enter number: "))
product=1
while num>0:
    digit=num%10
    if digit%2==0:
        product=product*digit
    num=num//10
print("product of even digits:",product)
 

num = int(input("Enter number: "))

even_count = 0
odd_count = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

    num = num // 10

print("Even digits:", even_count)
print("Odd digits:", odd_count)

  