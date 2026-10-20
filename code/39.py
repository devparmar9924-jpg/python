f=open("student.txt", "r")
data=f.readlines()
print("Total lines:", len(data))
f.close()