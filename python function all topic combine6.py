def student_details(**kwargs):
    print("name:", kwargs["name"])
    print("branch:", kwargs["branch"])
def calculate_total(*args):
    total=0
    for i in args:
        total=total+i
    return total
def check_result(total, pass_marks=35):
    if  total >= pass_marks:
        return "pass"
    else:
        return "fail"
def show_result():
    student_details( name="preetham",branch= "cds")
    total=calculate_total(30,40,50)
    resut=check_result(total)
    print("total:", total)
    print("result:", resut)
show_result()
def student_details(**kwargs):
    print("Name:", kwargs["name"])
    print("Branch:", kwargs["branch"])


def calculate_total(*args):
    total = 0

    for mark in args:
        total = total + mark

    return total


def check_grade(total, pass_marks=35):
    if total < pass_marks:
        return "Fail"
    elif total >= 225:
        return "A"
    elif total >= 180:
        return "B"
    elif total >= 150:
        return "C"
    else:
        return "Pass"


def show_result():
    student_details(name="Preetham", branch="Data Science")

    total = calculate_total(80, 75, 85)

    result = check_grade(total)

    print("Total:", total)
    print("Result:", result)

show_result()

def employee_details(**kwargs):
    print("Name:", kwargs["name"])
    print("Job:", kwargs["job"])


def calculate_salary(*args):
    total = 0

    for salary in args:
        total = total + salary

    return total


def add_bonus(total, bonus=10):
    bonus_amount = total * bonus / 100
    final_salary = total + bonus_amount

    return bonus_amount, final_salary


def check_salary(final_salary):
    if final_salary >= 50000:
        return "High Salary"
    else:
        return "Normal Salary"


def show_employee():
    employee_details(name="Preetham", job="Developer")

    total = calculate_salary(30000, 15000, 10000)

    bonus, final_salary = add_bonus(total)

    salary_type = check_salary(final_salary)

    print("Total Salary:", total)
    print("Bonus:", bonus)
    print("Final Salary:", final_salary)
    print("Salary Type:", salary_type)


show_employee()