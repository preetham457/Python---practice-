
num=int(input("enter the number: "))
even=0
odd=0
while num>0:
    digit=num%10
    if digit%2==0:
        even=even+1
    else:
        odd=odd+1
    num=num//10
print("even:",even)
print("odd:", odd)




num=int(input("enter the number: "))
count=0
while num>0:
    digit=num%10
    count=count+1
    num=num//10
print("count the number:", count) 
smallest=None

for i in range(10):
    num=int(input("enter the number: "))
    if smallest is None or num<smallest:
        smallest=num
print("samllest:", smallest)

num=int(input("enter the number: "))
reverse=0
while num>0:
    digit=num%10
    reverse=digit+1
    num=num//10
print("reverse the number:", reverse)


num=int(input("enter the number: "))
original=num
reverse=0

while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
if original==reverse:
    print("palindrome")
else:
    print(" not palindrome")


num=int(input("enter the number: "))
count=0
while num<0:
    digit=num%10
    if digit%2==0:
        even=even+1
    else:
        odd=odd+1
    num=num//10
print("even ")
print("odd")



