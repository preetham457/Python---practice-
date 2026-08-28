total = 0

for i in range(5):

    price = int(input("Enter item price: "))

    total = total + price

print("Total:", total)

if total >= 5000:
    discount = total * 20 / 100

elif total >= 3000:
    discount = total * 10 / 100

elif total >= 1000:
    discount = total * 5 / 100

else:
    discount = 0

final_bill = total - discount

print("Discount:", discount)
print("Final Bill:", final_bill)


correct_username = "admin"
correct_password = "1234"

login_success = False

for i in range(3):

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
        login_success = True
        break
    else:
        print("Invalid username or password")

if login_success == False:
    print("Account locked")