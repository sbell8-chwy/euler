import itertools


def e_converg(count):
    g = e_den()
    vals = list(itertools.islice(e_den(), 0, count, 1))
    num = 0
    den = 1
    for v in vals[::-1]:
        num = v * den + num
        num, den = den, num
    return 2 * den + num


def e_den():
    i = 1
    while True:
        yield 1
        yield 2*i
        yield 1
        i += 1
