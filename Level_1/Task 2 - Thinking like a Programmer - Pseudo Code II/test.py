n = 8

count = 0

n1 = 0
n2 = 1
f_nums= []

if n == 1:
    print(0)
else:
    while count < n:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        f_nums.append(n1)
        count += 1
print(f_nums)