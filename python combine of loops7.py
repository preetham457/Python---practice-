num=int(input("enter a number:"))
largest=0
while num>0:
    digit=num%10
    if digit>largest:
        largest=digit
    num=num//10
print("largest:", largest)



num=int(input("enter a number:"))
target=int(input("enter the digit:"))
count=0
while num>0:
    digit=num%10
    if digit==target:
        count=count+1
    num=num//10
print("count:", count)
num = int(input("Enter the number: "))

smallest = 9

while num > 0:

    digit = num % 10

    if digit < smallest:
        smallest = digit

    num = num // 10

print("Smallest digit:", smallest)



balance = 5000

while True:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance = balance + amount
        print("Deposit successful")

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")


   
    
    
    


