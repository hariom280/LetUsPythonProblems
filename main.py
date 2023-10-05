a = [1, 3, 5, 7, 9]
b = [2, 4, 6, 8, 10]

a = a + b
print(a)

a = [11, 17, 29] + a
print(a)

num = len(a)
print(num)

a[num - 3:num] = [100, 200, 300]
print(a)

a[:] = []
print(a)
del a

print(a)