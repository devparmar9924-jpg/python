f=open("student.txt", "r")
data=f.read()
word=input("Enter a word to search: ")
if word in data:
    print("Word found")
else:
    print("Word not found")
f.close()