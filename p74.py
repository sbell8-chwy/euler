import math


def factor_chain(limit=10**6):
    values = [0]*limit
    i = 1
    while i < limit:
        if values[i] == 0:
            values[i] = get_count([i], i, values)
        i += 1
    count = 0
    for v in values:
        if v == 60:
            count += 1
    return count, values


def get_count(chain, num, values):
    sf = sum_factorials(num)
    if len(values) > sf and values[sf] != 0:
        return len(chain) + values[sf]
    if sf in chain:
        if len(values) > sf:
            val = len(chain) - chain.index(sf)
            values[sf] = val
        return len(chain)
    return get_count(chain + [sf], sf, values)


def sum_factorials(num):
    digits = list(str(num))
    total = 0
    for d in digits:
        total += math.factorial(int(d))
    return total
