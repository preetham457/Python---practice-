def  welcome(name,message="good moring"):
    print(name,message)
welcome("preetham")
welcome("rahul","hi")

def bill(price,tax=50):
   sum=price+tax
   print(sum)
bill(10)
bill(40,50)

def employee(name,salary,department):
    print(name,salary,department)
employee("preetham",100000,"cds")

def add(*hh):
    total=0
    for num in hh:
        total=total+num
    print(total)
add(10,90,90,80,89,0,)

def find_largrst(*args):
    largest=0
    for num in args:
        if num>largest:
            largest=num
    print(largest)
find_largrst(10,20,30,40,90)

balance = 1000

def add_money():
    global balance
    balance = balance + 500

add_money()
print(balance)





x = 10

def test():
    x = 20
    print(x)

test()
print(x)