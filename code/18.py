#remove pop delete clear function
name=["dev","rahul","himanshu","ansh","kevin"]

#remove() by value
name.remove("ansh")
print(name)

#pop() return and remove last items
last=name.pop()
print(name)
print(last)

#delete by index
del name[1]
print(name)

#clear() emptirs everything
name.clear()
print(name)