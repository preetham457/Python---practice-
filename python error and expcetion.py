try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ValueError:
    print("Please enter a number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)
try:
    number = int(input("Enter a number: "))
    result = 10 / number

except ValueError:
    print("Please enter a number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program finished.")