def myfun(a, b):
    a = a.split('.')
    b = b.split('.')
    n = max(len(a), len(b))
    a = a + [0] * (n - len(a))
    b = b + [0] * (n - len(b))

    for i in range(n):
        x = int(a[i])
        y = int(b[i])
        if x > y:
            return 1
        elif x < y:
            return -1
    return 0


a = input('version1 = ')
b = input('version2 = ')
res = myfun(a, b)
print('输出: ', res)
