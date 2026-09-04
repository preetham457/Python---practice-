def customer_detalis(**kwargs):
    print("name:", kwargs["name"])
    print("city:", kwargs["city"])
def calculate_total(*args):
    total=0
    for price in args:
        total=total+price
    return total
def apply_discount(total,discount=10):
    discount_amount=total*discount/100
    finally_amount=total-discount_amount
    return  discount_amount , finally_amount
def check_order(finally_amount):
    if finally_amount>=1000:
        return "high price"
    else:
        return "normal price"
def show_order():
    customer_detalis(name="preetham",city="davanger")
    total=calculate_total(10,88,53)
    discount_amount,finally_amount=apply_discount(total)
    order_type=check_order(finally_amount)
    print("total:", total)
    print("discount:", discount_amount)
    print("final price:", finally_amount)
    print("order type;", order_type)
show_order()


def account_detalis(**kwargs):
    print("name:", kwargs["name"])
    print("account type:", kwargs["account_type"])
def calculate_balnce(*args):
    balance=0
    for desposit in args:
        balance=balance+desposit
    return balance
def check_balance(balance, minium_balance=1000):
    if balance>= minium_balance:
        return "high"
    else:
        return"noraml"
def show_account():
    account_detalis(name="preetham",account_type="sbi")
    balance = calculate_balnce(80, 100, 2000)

    result = check_balance(balance)

    print("Balance:", balance)
    print("Status:", result)

show_account()