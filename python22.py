num=int(input("Enter a number: "))

reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

print("Reverse:", reverse)

num=int(input("Enter a number: "))
even_sun=0
odd_product=1

while num>0:
    digit=num%10
    if digit%2==0:
        even_sun=even_sun+digit
    else:
        odd_product=odd_product*digit
    num=num//10

print("sum of even digits:",even_sun)
print("product of odd digits:",odd_product)


num=int(input("Enter a number: "))
smallest=9
while num>0:
    digit=num%10
    if digit<smallest:
        smallest=digit
    num=num//10
print("smallest digits:", smallest)


    
        

