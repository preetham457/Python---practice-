positive=0
negative=0
zero=0
total=0
largest=None
for i in range (10):
    num=int(input("enter the num: "))
    if num>0:
        positive = positive + 1
    elif num<0:
        negative = negative + 1
    else:
        zero=zero+1
    total=total+num
    if largest is None or num > largest:
        largest = num
print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)
print("Total:", total)
print("Largest:", largest)