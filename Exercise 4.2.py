a = [10, 20, 30, 40, 50]
b = a
b[1]=25
print(a)
# a is also changed
c = a[:]
print(c)
c[2]=35
print(a)
# a is also changed