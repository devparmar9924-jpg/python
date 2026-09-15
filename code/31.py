#find even odd using comprehension method
n=[10,45,29,40,2,5,7,9,56,67,89]

even = [i for i in n if i % 2 == 0]
odd = [i for i in n if i % 2 != 0]
print("Even =", even)
print("Odd =", odd)