num=int(input("enter the number:"))
total=0
while num>0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of digits:", total)
    

    






