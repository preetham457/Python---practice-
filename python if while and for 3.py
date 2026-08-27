secrect=7
num=int(input("guess the scerect key: "))
if num==secrect:
    print("correct")
else:
    print("wrong")


secret = 7

while True:
    num = int(input("Guess the secret number: "))

    if num == secret:
        print("Correct!")
        break
    elif num > secret:
        print("Too high")
    else:
        print("Too low")

even = 0
odd = 0
total = 0

for i in range(10):

    num = int(input("Enter number: "))

    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

    total = total + num

print("Even numbers:", even)
print("Odd numbers:", odd)
print("Total:", total)