username="preetham"
password=123
for i in range(3):
    user=input("enter the username: ")
    pwd=int(input("enter the password: "))
    if user==username and pwd==password:
        print("correct")
        break
    else:
        print("wrong")



username = "admin"
password = "1234"

for i in range(3):

    user = input("Enter username: ")
    pwd = input("Enter password: ")

    if user == username and pwd == password:
        print("Login successful")
        break

    else:
        print("Invalid username or password")

else:
    print("Account locked")

scecret=25
for i in range(3):
    code=int(input("enter the scecret"))
    if code==scecret:
        print("correct")
        break
    elif code>scecret:
        print("two high")
    elif code<scecret:
        print("two low")
    else:
       print ("locked")
else:
    print("game over")

password=int(input("enter the password: "))
for i in range(3):
    if password<8:
        print("strong password")
    elif password>8:
        print("medium password")
assword = input("Enter password: ")

has_number = False

for char in password:
    if char.isdigit():
        has_number = True
        break

if len(password) >= 8 and has_number:
    print("Strong Password")
else:
    print("Weak Password")


positive=0
negative=0
zero=0
total=0
largest=None
for i in range (10):
    num=int(input("enter the code: "))
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


    




    