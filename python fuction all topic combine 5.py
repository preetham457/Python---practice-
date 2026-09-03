multi= lambda a,b:a*b
print(multi(2,4))
is_even = lambda x: x % 2 == 0

print(is_even(8))
check = lambda x: "_postive_" if x > 0 else "__negative__"
print(check(7))

# comnbine topic

def calculate_total(*args):
    total=0
    for marks in args:
        total=total+marks
    return total
def check_result(total):
    if total>=105:
        return("pass")
    else:
        return("fali")
def show_result():
    total=calculate_total(100,3,4)
    result=check_result(total)
    print("total:", total)
    print("result:", result)

show_result()


def student_detalis(**kwargs):
    print( )
def student_details(**kwargs):
    print("Name:", kwargs["name"])
    print("Branch:", kwargs["branch"])


def calculate_total(*args):
    total = 0

    for mark in args:
        total = total + mark

    return total


def check_result(total):
    if total >= 105:
        return "Pass"
    else:
        return "Fail"


def show_result():
    student_details(name="Preetham", branch="Data Science")

    total = calculate_total(80, 75, 90)
    result = check_result(total)

    print("Total:", total)
    print("Result:", result)


show_result()  




def calculate_total(*args):
    total = 0

    for price in args:
        total = total + price

    return total


def apply_discount(total, discount=10):
    discount_amount = total * discount / 100
    final_price = total - discount_amount

    return final_price


def check_bill(price):
    if price >= 1000:
        return "High Bill"
    else:
        return "Normal Bill"


def show_bill():
    total = calculate_total(400, 300, 500)
    final_price = apply_discount(total)
    bill_type = check_bill(final_price)

    print("Total:", total)
    print("Final Price:", final_price)
    print("Bill Type:", bill_type)


show_bill()
   

    


