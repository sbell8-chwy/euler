import math

def f():
    upper = 10000
    count = 0
    n = 2
    while n <= upper:
        a0 = int(math.sqrt(n))
        if a0 * a0 == n:
            n += 1
            continue
        period = 0
        d = 1
        m = 0
        a = a0
        while True:
            m = d * a - m
            d = (n - m * m) / d
            a = (a0 + m) / d
            period += 1
            if a == 2*a0:
                break
        if period % 2 == 1:
            count += 1
        n += 1
    return count
