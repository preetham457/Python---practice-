num=int(input("enter the number:"))
count=0

while num>0:
    digit=num%10
    if digit%2!=0:
        count=count+1
    num=num//10
print("odd digits:",count)


num=int(input("enter the number:"))
smallest=9


while num>0:
    digit=num%10
    if digit<smallest:
        smallest=digit
    num=num//10
print("smallest digits", smallest)

    
num=int(input("enter the number:"))
count=0
while num>0:
    digit=num%10
    if digit==5:
        count=count+1
    num=num//10
print("number of 5:", count)


num=int(input("enter the number:"))
original=num
reverse=0
while num>0:
    digit=num%10
    rverse=reverse*10+digit
    num=num//10
if original==reverse:
    print("palindrome")
else:
    print("not palindrome")

num=int(input("enter the number:"))

even_count = 0
odd_count = 0
while num>0:
    digit=num%10
    if digit%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1

num=num//10
print("Even digits:", even_count)
print("Odd digits:", odd_count)



num=int(input("enter the number:"))
even_count=0
odd_count=0
while num>0:
    digit=num%10
    if digit % 2 == 0:
        even_sum = even_sum + digit
    else:
        odd_sum = odd_sum + digit

    num = num // 10

print("Sum of even digits:", even_sum)
print("Sum of odd digits:", odd_sum)

num = int(input("Enter number: "))

original = num
largest = 0

# Step 1: Find the largest digit
while num > 0:
    digit = num % 10

    if digit > largest:
        largest = digit

    num = num // 10

# Step 2: Count how many times largest appears
num = original
count = 0

while num > 0:
    digit = num % 10

    if digit == largest:
        count = count + 1

    num = num // 10

print("Largest digit:", largest)
print("Largest digit appears:", count, "times")

        
    

    


