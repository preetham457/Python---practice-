num = int(input("Enter number: "))
largest=0
while num>0:
    digit=num%10
    if digit>largest:
        largest=digit
        
    num=num//10
print("largst digit:",largest)


num = int(input("Enter number: "))
largest=0
smallest=9
while num>0:
    digit=num%10
    if digit>largest:
        largest=digit
    if digit<smallest:
        smallest=digit

    num=num//10
difference=largest-smallest

print("Largest digit:", largest)
print("Smallest digit:", smallest)
print("Difference:", difference)

num = int(input("Enter number: "))
search_digit=int(input("enter the digit to find:"))
count=0
while num>0:
    digit=num%10
    if digit==search_digit:
        count=count+1
    num=num//10
print("frequency of digit;", count)


for i in range(3):

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


for i in range(3):

    num = int(input("Enter number: "))

    even_sum = 0
    odd_sum = 0

    while num > 0:

        digit = num % 10

        if digit % 2 == 0:
            even_sum = even_sum + digit
        else:
            odd_sum = odd_sum + digit

        num = num // 10

    print("Sum of even digits:", even_sum)
    print("Sum of odd digits:", odd_sum)

secret_number = 7

for attempt in range(3):

    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Correct! 🎉")
        break
    else:
        print("Wrong guess!")

