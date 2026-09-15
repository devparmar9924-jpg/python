#sum of even and odd no. in given list
n=[10,45,29,40,2,5,7,9,56,67,89]
odd = 0
even = 0
for i in n:
    if i % 2 == 0:
        even += i
    else:
        odd += i

print("Even Totan =", even)
print("Odd Totan =", odd)