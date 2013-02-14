import euler_tools as et
import math

def xdy(max_d):
    x = 1.0
    y = 1.0
    large_x = 0
    for d in range(max_d, max_d + 1):
        if et.is_sqr(d):
            continue
        x2 = x**2
        y2 = d * (y**2)
        a = x2 - y2
        while a != 1:
            if a > 1:
                y += 1.0
                y2 = d * (y**2)
            if a < 1:
                x = next_x(y2)
                x2 = x**2
            a = x2 - y2
            print '%d - %d = %d' % (x, y, a)
        if x > large_x:
            large_x = x
        x, y = 1.0, 1.0
    return large_x


def test_one(d):
    x = 1.0
    y = 1.0
    x2 = x**2
    y2 = d * (y**2)
    a = x2 - y2
    while a != 1:
        if a > 1:
            y += 1
            y2 = d * (y**2)
        if a < 1:
            x += 1
            x2 = x**2
        a = x2 - y2
    return x

def next_x(y2):
    if et.is_sqr(y2 + 1):
        return math.sqrt(y2 + 1)
    return int(math.sqrt(y2)) + 1.0


def next_y(x2, d):
    temp = (x2 - 1.0) / d
    if et.is_sqr(temp):
        return math.sqrt(temp)
    return int(math.sqrt(temp)) + 1.0
