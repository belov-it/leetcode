def merge(a, b):
    c = []
    i = 0
    j = 0
    for i in range(0, len(a)):
        while(j < len(b) and b[j] < a[i]):
            c.append(b[j])
            j += 1
        c.append(a[i])
    while(j < len(b)):
        c.append(b[j])
        j += 1
    return c


a = [1, 3, 5]
b = [1, 2, 2, 4, 7]

merge(a, b)
