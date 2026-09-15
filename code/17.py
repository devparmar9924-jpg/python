#  Fibonic series

n = int ( input ( "Enter The Number:" ))
x=0
y=1
count = 0

while ( count < n ):
    print (x)
    c = x + y
    x = y
    y = c
    count = count + 1