try:
    f=open("marks.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("file not found")