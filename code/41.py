try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("answer:", a / b)
except ZeroDivisionError:
    print("cannot divide by zero")