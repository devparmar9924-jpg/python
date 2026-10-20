try:
    a=int(input("enter a number: "))
    b=int(input("enter another number: "))
    result=a+b
except ValueError:
    print("invalid input")
else:
    print("sum:",result)