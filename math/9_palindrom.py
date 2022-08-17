def isPal(num):
    if (num < 0):
        return False
    c = 0
    ost = num
    while(ost > 0):
        ost = ost // 10
        c += 1
    dl = num
    ost = num
    mid = c // 2
    for i in range(0, mid):
        if (dl//(10)**(c-1) == ost % 10):
            ost = ost // 10
            dl = dl % (10 ** (c-1))
            c -= 1
        else:
            return False
    return True


print(isPal(1))
