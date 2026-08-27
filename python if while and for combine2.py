units = int(input("Enter units: "))

if units <= 100:
    bill = units * 2

elif units <= 200:
    bill = (100 * 2) + ((units - 100) * 3)

else:
    bill = (100 * 2) + (100 * 3) + ((units - 200) * 5)

print("Total electricity bill: ₹", bill)



balance = 10000

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
        print("Balance:", balance)

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
            print("Balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
