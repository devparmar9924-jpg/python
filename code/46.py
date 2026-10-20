try:
    num=int(input("enter a number: "))
    print("number:", num)
except ValueError:
    print("invalid number")
finally:
    print("program ended")